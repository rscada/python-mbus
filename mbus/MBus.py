"""
Python bindings for rSCADA libmbus.
"""

from ctypes import c_int,c_char_p,addressof,pointer

from mbus.MBusFrame import MBusFrame
from mbus.MBusFrameData import MBusFrameData

class MBus:
    """
    A class to communicate to a device via MBus.
    """

    _libmbus = None

    def __init__(self, *args, **kwargs):
        """
        Constructor for MBus class.

        possible arguments are
        * device
        * host
        * libpath: path to libmbus (shared object or dll)
        * port: default 8888
        """

        import os
        from ctypes import cdll

        # check all given arguments for validity
        validargs = ('device','host','libpath','port')
        for arg in kwargs.keys():
            if arg not in validargs:
                raise TypeError("invalid argument")

        # set default values
        device = None
        host = None
        port = 8888
        libpath = None

        if 'device' in kwargs.keys():
             device = kwargs['device']

        if 'libpath' in kwargs.keys():
            libpath = kwargs['libpath']

        if 'host' in kwargs.keys():
            host = kwargs['host']

        if 'port' in kwargs.keys():
            if isinstance(kwargs['port'],int):
                if 65535 <= kwargs['port']:
                    raise ValueError("port number too high")
                if 0 > kwargs['port']:
                    raise ValueError("port number too low")
                port = kwargs['port']
            else:
                raise TypeError("port number not given as integer")

        if None == libpath:
            libpath = "/usr/local/lib/libmbus.so"

        self._libmbus = cdll.LoadLibrary(libpath)

        try:
            self._libmbus.mbus_get_current_version()
        except AttributeError:
            raise OSError("libmbus not found")

        if (None != device) and (None != host):
            raise BaseException("conflicting arguments 'device' and 'host' given")

        if (None == device) and (None == host):
            raise BaseException("Must provide either device or host keyword arguments")


        if device:
            fd = os.open(device, os.O_RDONLY)
            if not os.isatty(fd):
                raise TypeError(device+" is not a TTY")
            os.close(fd)
            self.handle = self._libmbus.mbus_context_serial(device)
        elif host != None and port:
            self.handle = self._libmbus.mbus_context_tcp(host)

    def connect(self):
        """
        Connect to MBus.
        """
        if self.handle:
            if self._libmbus.mbus_connect(self.handle) == -1:
                raise Exception("libmbus.mbus_connect failed")
        else:
            raise Exception("Handle object not configure")

    def disconnect(self):
        """
        Disconnect from MBus.
        """
        if self.handle:
            if self._libmbus.mbus_disconnect(self.handle) == -1:
                raise Exception("libmbus.mbus_disconnect failed")
        else:
            raise Exception("Handle object not configure")

    def send_request_frame(self, address):
        """
        Low-level function: send an request frame to the given address.
        """
        if self.handle:
            if self._libmbus.mbus_send_request_frame(
                    self.handle, c_int(address)) == -1:
                raise Exception("libmbus.mbus_send_request_frame failed")
        else:
            raise Exception("Handle object not configure")

    def recv_frame(self):
        """
        Low-level function: receive a request frame.
        """

        if not self.handle:
            raise Exception("Handle object not configure")

        reply = MBusFrame()

        if self._libmbus.mbus_recv_frame(self.handle, addressof(reply)) != 0:
            raise Exception("libmbus.mbus_recv_frame failed")

        return reply

    def frame_data_parse(self, reply):
        """
        Low-level function: parse data in frame.
        """

        reply_data = MBusFrameData()

        if self._libmbus.mbus_frame_data_parse(addressof(reply), addressof(reply_data)) != 0:
            raise Exception("libmbus.mbus_frame_data_parse failed")

        return reply_data

    def frame_data_xml(self, reply_data):
        """
        Low-level function: convert reply data frame to xml.
        """

        mbus_frame_data_xml = self._libmbus.mbus_frame_data_xml
        mbus_frame_data_xml.restype = c_char_p
        xml_result = mbus_frame_data_xml(pointer(reply_data))

        if not xml_result:
            raise Exception("libmbus.mbus_frame_data_xml failed")

        return xml_result
