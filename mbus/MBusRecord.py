from ctypes import Structure, Union, c_char_p, c_double, c_int, c_byte, \
        c_long, POINTER

c_byte_p = POINTER(c_byte)


class MBusString(Structure):
    _fields_ = [
            ('value',       c_byte_p),
            ('size',        c_int),
    ]


class MBusValue(Union):
    _fields_ = [
            ('real_val',    c_double),
            ('str_val',     MBusString),
    ]


class MBusRecord(Structure):
    _fields_ = [
            ('value',           MBusValue),
            ('is_numeric',      c_byte),
            ('unit',            c_char_p),
            ('function_medium', c_char_p),
            ('quantity',        c_char_p),
            ('device',          c_int),
            ('tariff',          c_long),
            ('storage_number',  c_long),
    ]
