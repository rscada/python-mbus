from ctypes import *

libmbus = None
try:
    libmbus = cdll.LoadLibrary('libmbus.so')
except OSError:
    libmbus = cdll.LoadLibrary('/usr/local/lib/libmbus.so')

if None == libmbus:
    raise OSError("libmbus not found")

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
