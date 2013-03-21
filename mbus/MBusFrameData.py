from ctypes import *

libmbus = None
try:
    libmbus = cdll.LoadLibrary('libmbus.so')
except OSError:
    libmbus = cdll.LoadLibrary('/usr/local/lib/libmbus.so')

if None == libmbus:
    raise OSError("libmbus not found")

class MBusFrameData(Structure):
    _fields_ = [("data_var",   c_uint8 * 16), # MBusFrameFixed
                ("data_fixed", c_uint8),
                ("type",       c_uint32),
                ("error",      c_uint32)]

    def __str__(self):
        return "MBusFrame: XXX"

