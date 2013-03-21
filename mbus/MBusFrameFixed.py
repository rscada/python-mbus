class MBusFrameFixed(Structure):
    _fields_ = [("id_bcd",     c_uint8 * 4),
                ("tx_cnt",     c_uint8),
                ("status",     c_uint8),
                ("cnt1_type",  c_uint8),
                ("cnt2_type",  c_uint8),
                ("cnt1_val",   c_uint8 * 4),
                ("cnt2_val",   c_uint8 * 4)]

    def __str__(self):
        return "MBusFrameVariable: XXX"
