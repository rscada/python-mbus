from ctypes import Structure, Union, c_int, c_byte, c_char_p


# Inner union
class MBusAddressInternal(Union):
    _fields_ = [
            ('primary',     c_int),
            ('secondary',   c_char_p),
    ]


class MBusAddress(Structure):
    _fields_ = [
            ('is_primary',  c_byte),
            ('_address',    MBusAddressInternal),
    ]

    @property
    def pri_address(self):
        if self.is_primary:
            return self._address.primary

    @pri_address.setter
    def pri_address(self, address):
        self._address.primary = address
        self.is_primary = 1

    @property
    def sec_address(self):
        if not self.is_primary:
            return self._address.secondary

    @sec_address.setter
    def sec_address(self, address):
        self._address.secondary = address
        self.is_primary = 0
