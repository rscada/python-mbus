from ctypes import Structure,c_uint8

class MBusDataVariableHeader(Structure):
    _fields_ = [("id_bcd",       c_uint8 * 4),
                ("manufacturer", c_uint8 * 2),
                ("version",      c_uint8),
                ("medium",       c_uint8),
                ("access_no",    c_uint8),
                ("status",       c_uint8),
                ("signature",    c_uint8 * 2)]

    def __str__(self):
        return "MBusDataVariableHeader: XXX"
