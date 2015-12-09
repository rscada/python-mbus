from ctypes import Structure,c_uint8,c_uint32
from enum import Enum

from mbus.MBusDataVariable import MBusDataVariable
from mbus.MBusDataFixed import MBusDataFixed


class MBusFrameDataType(Enum):
    '''
    ABSTRACT DATA FORMAT (error, fixed or variable length)
    '''
    Fixed =    1
    Variable = 2
    Error =    3


class MBusFrameError(Enum):
    '''
    GENERAL APPLICATION ERRORS
    '''
    Unspecified =     0x00
    UnimplementedCI = 0x01
    BufferTooLong =   0x02
    TooManyRecords =  0x03
    PrematureEnd =    0x04
    TooManyDIFes =    0x05
    TooManyVIFes =    0x06
    Reserved =        0x07
    ApplicationBusy = 0x08
    TooManyReadouts = 0x09


class MBusFrameData(Structure):

    _fields_ = [("data_var",   MBusDataVariable),
                ("data_fixed", MBusDataFixed),
                ("type",       c_uint32),
                ("error",      c_uint32)]

    def __str__(self):
        return "MBusFrameData: XXX"
