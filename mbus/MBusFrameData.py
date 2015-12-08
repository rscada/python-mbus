from ctypes import Structure,c_uint8,c_uint32

from mbus.MBusDataVariable import MBusDataVariable
from mbus.MBusDataFixed import MBusDataFixed

class MBusFrameData(Structure):
    #
    # ABSTRACT DATA FORMAT (error, fixed or variable length)
    #
    MBUS_DATA_TYPE_FIXED =    1
    MBUS_DATA_TYPE_VARIABLE = 2
    MBUS_DATA_TYPE_ERROR =    3

    _fields_ = [("data_var",   MBusDataVariable),
                ("data_fixed", MBusDataFixed),
                ("type",       c_uint32),
                ("error",      c_uint32)]

    def __str__(self):
        return "MBusFrameData: XXX"
