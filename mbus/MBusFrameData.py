from ctypes import Structure,c_uint8,c_uint32

from mbus.MBusDataVariable import MBusDataVariable
from mbus.MBusDataFixed import MBusDataFixed

class MBusFrameData(Structure):
    _fields_ = [("data_var",   MBusDataVariable),
                ("data_fixed", MBusDataFixed),
                ("type",       c_uint32),
                ("error",      c_uint32)]

    def __str__(self):
        return "MBusFrame: XXX"
