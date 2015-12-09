from ctypes import Structure, c_ubyte, c_size_t, c_long, POINTER

# TODO: is this correct?
c_time_t = c_long

class MBusDataInformationBlock(Structure):
    _fields_ = [
            ('dif',         c_ubyte),
            ('dife',        c_ubyte*10),
            ('ndife',       c_size_t),
    ]


class MBusValueInformationBlock(Structure):
    _fields_ = [
            ('vif',         c_ubyte),
            ('vife',        c_ubyte*10),
            ('nvife',       c_size_t),
            ('custom_vif',  c_ubyte*128),
    ]


class MBusDataRecordHeader(Structure):
    _fields_ = [
            ('dib',         MBusDataInformationBlock),
            ('vib',         MBusValueInformationBlock),
    ]


class MBusDataRecord(Structure):
    pass
MBusDataRecord._fields_ = [
            ('drh',         MBusDataRecordHeader),
            ('data',        c_ubyte * 234),
            ('data_len',    c_size_t),
            ('timestamp',   c_time_t),
            ('next',        POINTER(MBusDataRecord)),
    ]
