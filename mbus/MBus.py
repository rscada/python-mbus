"""
Python bindings for rSCADA libmbus.
"""

import os
from ctypes import *

libmbus = None
try:
    libmbus = cdll.LoadLibrary('libmbus.so')
except OSError:
    libmbus = cdll.LoadLibrary('/usr/local/lib/libmbus.so')

if None == libmbus:
    raise OSError("libmbus not found")


class MBus:
    """
    A class to communicate to a device via MBus.
    """

    def __init__(self, device=None, host=None, port=8888):
        """
        Constructor for MBus class.
        """

        if (None != device) and (None != host):
            raise BaseException("conflicting arguments given")

        if device:
            fd = os.open(device, os.O_RDONLY)
            if not os.isatty(fd):
                raise TypeError(device+" is not a TTY")
            os.close(fd)
            self.handle = libmbus.mbus_context_serial(device)
        elif host and port:
            self.handle = libmbus.mbus_context_tcp(host)
        else:
            raise BaseException(
                "Must provide either device or host keyword arguments")

    def connect(self):
        """
        Connect to MBus.
        """
        if self.handle:
            if libmbus.mbus_connect(self.handle) == -1:
                raise Exception("libmbus.mbus_connect failed")
        else:
            raise Exception("Handle object not configure")

    def disconnect(self):
        """
        Disconnect from MBus.
        """
        if self.handle:
            if libmbus.mbus_disconnect(self.handle) == -1:
                raise Exception("libmbus.mbus_disconnect failed")
        else:
            raise Exception("Handle object not configure")

    def send_request_frame(self, address):
        """
        Low-level function: send an request frame to the given address.
        """
        if self.handle:
            if libmbus.mbus_send_request_frame(
                    byref(self.handle), c_int(address)) == -1:
                raise Exception("libmbus.mbus_send_request_frame failed")
        else:
            raise Exception("Handle object not configure")

    def recv_frame(self):
        """
        Low-level function: receive a request frame.
        """

        if self.handle:
            raise Exception("Handle object not configure")

        reply = MBusFrame()

        if libmbus.mbus_recv_frame(byref(self.handle), byref(reply)) != 0:
            raise Exception("libmbus.mbus_recv_frame failed")

        return reply

    def frame_data_parse(self, reply):
        """
        Low-level function: parse data in frame.
        """

        reply_data = MBusFrameData()

        if libmbus.mbus_frame_data_parse(byref(reply), byref(reply_data)) != 0:
            raise Exception("libmbus.mbus_frame_data_parse failed")

        return reply_data

    def frame_data_xml(self, reply_data):
        """
        Low-level function: convert reply data frame to xml.
        """

        xml_result = libmbus.mbus_frame_data_xml(byref(reply_data))

        return reply_data
