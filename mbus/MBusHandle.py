from ctypes import Structure, c_uint32, c_uint8, c_void_p, c_int, c_byte

class MBusHandle(Structure):
    _fields_ = [("fd",                  c_int),
                ("max_data_retry",      c_int),
                ("max_search_retry",    c_int),
                ("purge_first_frame",   c_byte),
                ("is_serial",           c_uint8),
                ("internal",            c_void_p * 10)]  # pointers

    def __str__(self):
        return "MBusHandle: XXX"
