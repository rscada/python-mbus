#!/usr/bin/python
# ------------------------------------------------------------------------------
# Copyright (C) 2012, Robert Johansson <rob@raditex.nu>, Raditex Control AB
# All rights reserved.
# ------------------------------------------------------------------------------

"""
Python bindings for rSCADA libmbus.
"""

from ctypes import *

libmbus = None
try:
    libmbus = cdll.LoadLibrary('libmbus.so')
except OSError:
    libmbus = cdll.LoadLibrary('/usr/local/lib/libmbus.so')

if None == libmbus:
    raise OSError("libmbus not found")
    
class MBusHandle(Structure):
    _fields_ = [("fd",        c_uint32),
                ("is_serial", c_uint8),
                ("internal",  c_uint32 * 6)] # pointers

    def __str__(self):
        return "MBusHandle: XXX"

class MBusFrameFixed(Structure):
    _fields_ = [("id_bcd",     c_uint8 * 4),
                ("tx_cnt",     c_uint8),
                ("status",     c_uint8),
                ("cnt1_type",  c_uint8),
                ("cnt2_type",  c_uint8),
                ("cnt1_val",   c_uint8 * 4),
                ("cnt2_val",   c_uint8 * 4)]

    def __str__(self):
        return "MBusFrameVariable: XXX"

class MBusFrameFixed(Structure):
    _fields_ = [("id_bcd",     c_uint8 * 4),
                ("tx_cnt",     c_uint8),
                ("status",     c_uint8),
                ("cnt1_type",  c_uint8),
                ("cnt2_type",  c_uint8),
                ("cnt1_val",   c_uint8 * 4),
                ("cnt2_val",   c_uint8 * 4)]

    def __str__(self):
        return "MBusFrameFixed: XXX"

class MBusFrame(Structure):
    _fields_ = [("start1",   c_uint8 * 16), # MBusFrameFixed
                ("length1",  c_uint8),
                ("length2",  c_uint8),
                ("start2",   c_uint8),
                ("control",  c_uint8),
                ("address",  c_uint8),
                ("control_infomation",  c_uint8),
                ("checksum", c_uint8),
                ("stop",     c_uint8),
                ("data",     c_uint8 * 252),
                ("data_size", c_uint32), # check
                ("stop",      c_uint8),
                ("timestamp", c_uint32), # check
                ("next",      c_uint8)] # pointer

    def __str__(self):
        return "MBusFrame: XXX"


class MBusFrameData(Structure):
    _fields_ = [("data_var",   c_uint8 * 16), # MBusFrameFixed
                ("data_fixed", c_uint8),
                ("type",       c_uint32),
                ("error",      c_uint32)]

    def __str__(self):
        return "MBusFrame: XXX"


class MBus:

    def __init__(self, device=None, host=None, port=8888):
        """
        Constructor for MBus class.
        """

        if device:
            self.handle = libmbus.mbus_context_serial(device)
        elif address and port:
            self.handle = libmbus.mbus_context_tcp(host)
        else:
            raise Exception("Must provide either device or host keyword arguments")        

    def connect(self):
        """
        
        """
        if self.handle:
            if libmbus.mbus_connect(self.handle) == -1:
                raise Exception("libmbus.mbus_connect failed")        
        else: 
            raise Exception("Handle object not configure")                       

            
    def disconnect(self):
        """
        
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
            if libmbus.mbus_send_request_frame(byref(self.handle), c_int(address)) == -1:
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

