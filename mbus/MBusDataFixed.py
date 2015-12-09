from ctypes import Structure, c_uint8
from enum import Enum

class MBusDataFixedMedium(Enum):
    '''
    M-Bus Fixed data medium types.
    Reference: http://www.m-bus.com/mbusdoc/md8.php table 8.3.1.
    '''

    Other = 0x00
    Oil = 0x01
    Electricity = 0x02
    Gas = 0x03
    Heat = 0x04
    Steam = 0x05
    HotWater = 0x06
    Water = 0x07
    HCA = 0x08
    Reserved = 0x09
    GasMode2 = 0x0A
    HeatMode2 = 0x0B
    HotWaterMode2 = 0x0C
    WaterMode2 = 0x0D
    HCAMode2 = 0x0E
    Reserved = 0x0F


class MBusDataFixedUnit(Enum):
    '''
    M-Bus Fixed data units.
    Reference: http://www.m-bus.com/mbusdoc/md8.php table 8.3.2.
    '''

    HMS = 0x00
    DMY = 0x01

    WH = 0x02
    WH_10 = 0x03
    WH_100 = 0x04

    KWH = 0x05
    KWH_10 = 0x06
    KWH_100 = 0x07

    MWH = 0x08
    MWH_10 = 0x09
    MWH_100 = 0x0A

    KJ = 0x0B
    KJ_10 = 0x0C
    KJ_100 = 0x0E

    MJ = 0x0D
    MJ_10 = 0x0F
    MJ_100 = 0x10

    GJ = 0x11
    GJ_10 = 0x12
    GJ_100 = 0x13

    W = 0x14
    W_10 = 0x15
    W_100 = 0x16

    KW = 0x17
    KW_10 = 0x18
    KW_100 = 0x19

    MW = 0x1A
    MW_10 = 0x1B
    MW_100 = 0x1C

    KJPH = 0x1D
    KJPH_10 = 0x1E
    KJPH_100 = 0x1F

    MJPH = 0x20
    MJPH_10 = 0x21
    MJPH_100 = 0x22

    GJPH = 0x23
    GJPH_10 = 0x24
    GJPH_100 = 0x25

    ML = 0x26
    ML_10 = 0x27
    ML_100 = 0x28

    L = 0x29
    L_10 = 0x2A
    L_100 = 0x2B

    MMM = 0x2C
    MMM_10 = 0x2D
    MMM_100 = 0x2E

    MLPH = 0x2F
    MLPH_10 = 0x30
    MLPH_100 = 0x31

    LPH = 0x32
    LPH_10 = 0x33
    LPH_100 = 0x34

    MMMPH = 0x35
    MMMPH_10 = 0x36
    MMMPH_100 = 0x37

    DEG_C_1000 = 0x38
    HCA = 0x39

    RESERVED_3A = 0x3A
    RESERVED_3B = 0x3B
    RESERVED_3C = 0x3C
    RESERVED_3D = 0x3D
    RESERVED_HIST = 0x3E

    WITHOUT_UNITS = 0x3F


class MBusDataFixed(Structure):
    _fields_ = [("id_bcd",    c_uint8 * 4),
                ("tx_cnt",    c_uint8),
                ("status",    c_uint8),
                ("cnt1_type", c_uint8),
                ("cnt2_type", c_uint8),
                ("cnt1_val",  c_uint8 * 4),
                ("cnt2_val",  c_uint8 * 4)]

    @property
    def medium(self):
        '''
        Decode the medium from the fixed field data.
        '''
        # Medium is stored in the first two bits of each byte in medium/unit
        # field.
        return MBusDataFixedMedium(
                ((self.cnt1_type & 0xc0) >> 6) \
                        | ((self.cnt2_type & 0xc0) >> 4))

    @property
    def cnt1_unit(self, unit):
        '''
        Decode the unit of counter 1.
        '''
        return MBusDataFixedUnit(self.cnt1_type & 0x3f)

    @property
    def cnt2_unit(self, unit):
        '''
        Decode the unit of counter 1.
        '''
        return MBusDataFixedUnit(self.cnt2_type & 0x3f)

    def __str__(self):
        return "MBusDataFixed: XXX"
