"""
Python bindings for rSCADA libmbus.
"""

from ctypes import c_int,c_char_p,c_void_p,addressof,pointer,POINTER

from .MBusFrame import MBusFrame
from .MBusFrameData import MBusFrameData
from .MBusLowLevel import MBusLib

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

        try:
            self._libmbus = MBusLib(libpath)
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
            self.handle = self._libmbus.context_serial(device)
        elif host != None and port:
            self.handle = self._libmbus.context_tcp(host)

    def connect(self):
        """
        Connect to MBus.
        """
        if self.handle:
            if self._libmbus.connect(self.handle) == -1:
                raise Exception("libmbus.mbus_connect failed")
        else:
            raise Exception("Handle object not configure")

    def disconnect(self):
        """
        Disconnect from MBus.
        """
        if self.handle:
            if self._libmbus.disconnect(self.handle) == -1:
                raise Exception("libmbus.mbus_disconnect failed")
        else:
            raise Exception("Handle object not configure")

    def send_request_frame(self, address):
        """
        Low-level function: send an request frame to the given address.
        """
        if self.handle:
            if self._libmbus.send_request_frame(self.handle, c_int(address)) == -1:
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

        if self._libmbus.recv_frame(self.handle, reply) != 0:
            raise Exception("libmbus.mbus_recv_frame failed")

        return reply

    def frame_data_parse(self, reply):
        """
        Low-level function: parse data in frame.
        """

        reply_data = MBusFrameData()

        if self._libmbus.frame_data_parse(reply, reply_data) != 0:
            raise Exception("libmbus.mbus_frame_data_parse failed")

        return reply_data

    def frame_data_xml(self, reply_data):
        """
        Low-level function: convert reply data frame to xml.
        """

        xml_result = self._libmbus.frame_data_xml(reply_data)

        if not xml_result:
            raise Exception("libmbus.mbus_frame_data_xml failed")

        return xml_result
