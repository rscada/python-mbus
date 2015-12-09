from ctypes import Structure, c_uint8, c_size_t, c_char_p, POINTER

from .MBusDataVariableHeader import MBusDataVariableHeader
from .MBusDataRecord import MBusDataRecord

mbus_data_record_p = POINTER(MBusDataRecord)

class MBusDataVariable(Structure):
    _fields_ = [("header", MBusDataVariableHeader),
                ("record", mbus_data_record_p),
                ("nrecords", c_size_t),
                ("data", c_char_p),
                ("data_len", c_size_t),
                ("more_records_follow", c_uint8),
                ("mdh", c_uint8),
                ("mfg_data", c_char_p),
                ("mfg_data_len", c_size_t)]

    def __str__(self):
        return "MBusDataVariable: XXX"
