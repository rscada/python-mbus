"""
Low-level function call wrappers for libmbus
"""

from ctypes import c_int, c_long, c_longlong, c_char_p, c_void_p, \
        c_char, c_byte, c_ubyte, c_double, POINTER, cdll, c_size_t, c_uint16
from ctypes.util import find_library

from .MBusAddress import MBusAddress
from .MBusFrame import MBusFrame
from .MBusFrameData import MBusFrameData
from .MBusDataFixed import MBusDataFixed
from .MBusDataVariableHeader import MBusDataVariableHeader
from .MBusDataVariable import MBusDataVariable
from .MBusHandle import MBusHandle
from .MBusRecord import MBusRecord
from .MBusDataRecord import MBusDataRecord, MBusValueInformationBlock

c_char_pp = POINTER(POINTER(c_char))    # http://stackoverflow.com/a/13161052
c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)
c_long_p = POINTER(c_long)
c_longlong_p = POINTER(c_long)
c_ubyte_p = POINTER(c_ubyte)
c_tm_p = c_void_p

mbus_frame_p = POINTER(MBusFrame)
mbus_handle_p = POINTER(MBusHandle)
mbus_address_p = POINTER(MBusAddress)
mbus_record_p = POINTER(MBusRecord)
mbus_frame_data_p = POINTER(MBusFrameData)
mbus_data_record_p = POINTER(MBusDataRecord)
mbus_data_variable_p = POINTER(MBusDataVariable)
mbus_data_fixed_p = POINTER(MBusDataFixed)
mbus_slave_data_p = c_void_p # TODO
mbus_data_variable_header_p = POINTER(MBusDataVariableHeader)
mbus_value_information_block_p = POINTER(MBusValueInformationBlock)


# Constants used throughout MBUS.  Not all of these will be used by the API,
# but it's easier to haul them all out and stuff them in there than to try and
# curate the list.
#
# The following is generated against libmbus using the following command:
# $ sed -n -e 's/#define[ \t]\+\(MBUS_[A-Z0-0_]\+\)[ \t]\+\([0-9a-fx]\+\)$/\1 = \2/i p' ../libmbus/mbus/*.h
MBUS_PROBE_NOTHING = 0
MBUS_PROBE_SINGLE = 1
MBUS_PROBE_COLLISION = 2
MBUS_FRAME_PURGE_NONE = 0
MBUS_FRAME_DATA_LENGTH = 252
MBUS_HANDLE_TYPE_TCP = 0
MBUS_HANDLE_TYPE_SERIAL = 1
MBUS_RECV_RESULT_OK = 0
MBUS_DIB_DIF_WITHOUT_EXTENSION = 0x7F
MBUS_DIB_DIF_EXTENSION_BIT = 0x80
MBUS_DIB_VIF_WITHOUT_EXTENSION = 0x7F
MBUS_DIB_VIF_EXTENSION_BIT = 0x80
MBUS_DIB_DIF_MANUFACTURER_SPECIFIC = 0x0F
MBUS_DIB_DIF_MORE_RECORDS_FOLLOW = 0x1F
MBUS_DIB_DIF_IDLE_FILLER = 0x2F
MBUS_DATA_VARIABLE_HEADER_LENGTH = 12
MBUS_DATA_FIXED_LENGTH = 16
MBUS_DATA_TYPE_FIXED = 1
MBUS_DATA_TYPE_VARIABLE = 2
MBUS_DATA_TYPE_ERROR = 3
MBUS_FRAME_TYPE_ANY = 0x00
MBUS_FRAME_TYPE_ACK = 0x01
MBUS_FRAME_TYPE_SHORT = 0x02
MBUS_FRAME_TYPE_CONTROL = 0x03
MBUS_FRAME_TYPE_LONG = 0x04
MBUS_FRAME_ACK_BASE_SIZE = 1
MBUS_FRAME_SHORT_BASE_SIZE = 5
MBUS_FRAME_CONTROL_BASE_SIZE = 9
MBUS_FRAME_LONG_BASE_SIZE = 9
MBUS_FRAME_BASE_SIZE_ACK = 1
MBUS_FRAME_BASE_SIZE_SHORT = 5
MBUS_FRAME_BASE_SIZE_CONTROL = 9
MBUS_FRAME_BASE_SIZE_LONG = 9
MBUS_FRAME_FIXED_SIZE_ACK = 1
MBUS_FRAME_FIXED_SIZE_SHORT = 5
MBUS_FRAME_FIXED_SIZE_CONTROL = 6
MBUS_FRAME_FIXED_SIZE_LONG = 6
MBUS_FRAME_ACK_START = 0xE5
MBUS_FRAME_SHORT_START = 0x10
MBUS_FRAME_CONTROL_START = 0x68
MBUS_FRAME_LONG_START = 0x68
MBUS_FRAME_STOP = 0x16
MBUS_MAX_PRIMARY_SLAVES = 250
MBUS_CONTROL_FIELD_DIRECTION = 0x07
MBUS_CONTROL_FIELD_FCB = 0x06
MBUS_CONTROL_FIELD_ACD = 0x06
MBUS_CONTROL_FIELD_FCV = 0x05
MBUS_CONTROL_FIELD_DFC = 0x05
MBUS_CONTROL_FIELD_F0 = 0x01
MBUS_CONTROL_MASK_SND_NKE = 0x40
MBUS_CONTROL_MASK_SND_UD = 0x53
MBUS_CONTROL_MASK_RSP_UD = 0x08
MBUS_CONTROL_MASK_FCB = 0x20
MBUS_CONTROL_MASK_FCV = 0x10
MBUS_CONTROL_MASK_ACD = 0x20
MBUS_CONTROL_MASK_DFC = 0x10
MBUS_CONTROL_MASK_DIR = 0x40
MBUS_ADDRESS_BROADCAST_REPLY = 0xFE
MBUS_ADDRESS_BROADCAST_NOREPLY = 0xFF
MBUS_ADDRESS_NETWORK_LAYER = 0xFD
MBUS_CONTROL_INFO_DATA_SEND = 0x51
MBUS_CONTROL_INFO_DATA_SEND_MSB = 0x55
MBUS_CONTROL_INFO_SELECT_SLAVE = 0x52
MBUS_CONTROL_INFO_SELECT_SLAVE_MSB = 0x56
MBUS_CONTROL_INFO_APPLICATION_RESET = 0x50
MBUS_CONTROL_INFO_SYNC_ACTION = 0x54
MBUS_CONTROL_INFO_REQUEST_RAM_READ = 0xB1
MBUS_CONTROL_INFO_SEND_USER_DATA = 0xB2
MBUS_CONTROL_INFO_INIT_TEST_CALIB = 0xB3
MBUS_CONTROL_INFO_EEPROM_READ = 0xB4
MBUS_CONTROL_INFO_SW_TEST_START = 0xB6
MBUS_CONTROL_INFO_ERROR_GENERAL = 0x70
MBUS_CONTROL_INFO_STATUS_ALARM = 0x71
MBUS_CONTROL_INFO_RESP_FIXED = 0x73
MBUS_CONTROL_INFO_RESP_FIXED_MSB = 0x77
MBUS_CONTROL_INFO_RESP_VARIABLE = 0x72
MBUS_CONTROL_INFO_RESP_VARIABLE_MSB = 0x76
MBUS_DATA_FIXED_STATUS_FORMAT_MASK = 0x80
MBUS_DATA_FIXED_STATUS_FORMAT_BCD = 0x00
MBUS_DATA_FIXED_STATUS_FORMAT_INT = 0x80
MBUS_DATA_FIXED_STATUS_DATE_MASK = 0x40
MBUS_DATA_FIXED_STATUS_DATE_STORED = 0x40
MBUS_DATA_FIXED_STATUS_DATE_CURRENT = 0x00
MBUS_DATA_RECORD_DIF_MASK_INST = 0x00
MBUS_DATA_RECORD_DIF_MASK_MIN = 0x10
MBUS_DATA_RECORD_DIF_MASK_DATA = 0x0F
MBUS_DATA_RECORD_DIF_MASK_FUNCTION = 0x30
MBUS_DATA_RECORD_DIF_MASK_STORAGE_NO = 0x40
MBUS_DATA_RECORD_DIF_MASK_EXTENTION = 0x80
MBUS_DATA_RECORD_DIF_MASK_NON_DATA = 0xF0
MBUS_DATA_RECORD_DIFE_MASK_STORAGE_NO = 0x0F
MBUS_DATA_RECORD_DIFE_MASK_TARIFF = 0x30
MBUS_DATA_RECORD_DIFE_MASK_DEVICE = 0x40
MBUS_DATA_RECORD_DIFE_MASK_EXTENSION = 0x80
MBUS_ERROR_DATA_UNSPECIFIED = 0x00
MBUS_ERROR_DATA_UNIMPLEMENTED_CI = 0x01
MBUS_ERROR_DATA_BUFFER_TOO_LONG = 0x02
MBUS_ERROR_DATA_TOO_MANY_RECORDS = 0x03
MBUS_ERROR_DATA_PREMATURE_END = 0x04
MBUS_ERROR_DATA_TOO_MANY_DIFES = 0x05
MBUS_ERROR_DATA_TOO_MANY_VIFES = 0x06
MBUS_ERROR_DATA_RESERVED = 0x07
MBUS_ERROR_DATA_APPLICATION_BUSY = 0x08
MBUS_ERROR_DATA_TOO_MANY_READOUTS = 0x09
MBUS_VARIABLE_DATA_MEDIUM_OTHER = 0x00
MBUS_VARIABLE_DATA_MEDIUM_OIL = 0x01
MBUS_VARIABLE_DATA_MEDIUM_ELECTRICITY = 0x02
MBUS_VARIABLE_DATA_MEDIUM_GAS = 0x03
MBUS_VARIABLE_DATA_MEDIUM_HEAT_OUT = 0x04
MBUS_VARIABLE_DATA_MEDIUM_STEAM = 0x05
MBUS_VARIABLE_DATA_MEDIUM_HOT_WATER = 0x06
MBUS_VARIABLE_DATA_MEDIUM_WATER = 0x07
MBUS_VARIABLE_DATA_MEDIUM_HEAT_COST = 0x08
MBUS_VARIABLE_DATA_MEDIUM_COMPR_AIR = 0x09
MBUS_VARIABLE_DATA_MEDIUM_COOL_OUT = 0x0A
MBUS_VARIABLE_DATA_MEDIUM_COOL_IN = 0x0B
MBUS_VARIABLE_DATA_MEDIUM_HEAT_IN = 0x0C
MBUS_VARIABLE_DATA_MEDIUM_HEAT_COOL = 0x0D
MBUS_VARIABLE_DATA_MEDIUM_BUS = 0x0E
MBUS_VARIABLE_DATA_MEDIUM_UNKNOWN = 0x0F
MBUS_VARIABLE_DATA_MEDIUM_COLD_WATER = 0x16
MBUS_VARIABLE_DATA_MEDIUM_DUAL_WATER = 0x17
MBUS_VARIABLE_DATA_MEDIUM_PRESSURE = 0x18
MBUS_VARIABLE_DATA_MEDIUM_ADC = 0x19


class MBusLib(object):
    """
    MBusLib is a helper class that provides methods for calling libmbus'
    functions with correct argument and return value types.
    """

    def __init__(self, libpath=None):
        '''
        Load an instance of libmbus, optionally with the specified library
        path.
        '''
        if libpath is None:
            libpath = find_library('mbus')

        lib = cdll.LoadLibrary(libpath)

        # Define the methods from libmbus

        # mbus.h:
        self.init                           = lib.mbus_init
        self.init.restype                   = c_int

        self.get_current_version            = lib.mbus_get_current_version
        self.get_current_version.restype    = c_char_p

        # mbus-protocol-aux.h
        self.context_tcp                    = lib.mbus_context_tcp
        self.context_tcp.argtypes           = [c_char_p, c_uint16]
        self.context_tcp.restype            = mbus_handle_p

        self.context_serial                 = lib.mbus_context_serial
        self.context_serial.argtypes        = [c_char_p]
        self.context_serial.restype         = mbus_handle_p

        self.context_free                   = lib.mbus_context_free
        self.context_free.argtypes          = [mbus_handle_p]
        self.context_free.restype           = None

        self.connect                        = lib.mbus_connect
        self.connect.argtypes               = [mbus_handle_p]
        self.connect.restype                = c_int

        self.disconnect                     = lib.mbus_disconnect
        self.disconnect.argtypes            = [mbus_handle_p]
        self.disconnect.restype             = c_int

        self.context_set_option             = lib.mbus_context_set_option
        self.context_set_option.argtypes    = [mbus_handle_p, c_int, c_long]
        self.context_set_option.restype     = c_int

        self.recv_frame                     = lib.mbus_recv_frame
        self.recv_frame.argtypes            = [mbus_handle_p, mbus_frame_p]
        self.recv_frame.restype             = c_int

        self.purge_frames                   = lib.mbus_purge_frames
        self.purge_frames.argtypes          = [mbus_handle_p]
        self.purge_frames.restype           = c_int

        self.send_frame                     = lib.mbus_send_frame
        self.send_frame.argtypes            = [mbus_handle_p, mbus_frame_p]
        self.send_frame.restype             = c_int

        self.send_select_frame              = lib.mbus_send_select_frame
        self.send_select_frame.argtypes     = [mbus_handle_p, c_char_p]
        self.send_select_frame.restype      = c_int

        self.send_application_reset_frame   = \
                lib.mbus_send_application_reset_frame
        self.send_application_reset_frame.argtypes  = [mbus_handle_p, c_char_p]
        self.send_application_reset_frame.restype   = c_int

        self.send_switch_baudrate_frame   = lib.mbus_send_switch_baudrate_frame
        self.send_switch_baudrate_frame.argtypes    = [mbus_handle_p, c_int, \
                                                        c_long]
        self.send_switch_baudrate_frame.restype   = c_int

        self.send_request_frame             = lib.mbus_send_request_frame
        self.send_request_frame.argtypes    = [mbus_handle_p, c_int]
        self.send_request_frame.restype     = c_int

        self.send_user_data_frame           = lib.mbus_send_user_data_frame
        self.send_user_data_frame.argtypes  = [mbus_handle_p, c_int,
                                                c_ubyte_p, c_size_t]
        self.send_user_data_frame.restype   = c_int

        self.sendrecv_request               = lib.mbus_sendrecv_request
        self.sendrecv_request.argtypes      = [mbus_handle_p, c_int,
                                                mbus_frame_p, c_int]
        self.sendrecv_request.restype       = c_int

        self.select_secondary_address       = lib.mbus_select_secondary_address
        self.select_secondary_address.argtypes  = [mbus_frame_p, c_char_p]
        self.select_secondary_address.restype   = c_int

        self.probe_secondary_address        = lib.mbus_probe_secondary_address
        self.probe_secondary_address.argtypes   = [mbus_handle_p, c_char_p,
                                                    c_char_p]
        self.probe_secondary_address.restype    = c_int

        self.read_slave                     = lib.mbus_read_slave
        self.read_slave.argtypes            = [mbus_handle_p, mbus_address_p,
                                                mbus_frame_p]
        self.read_slave.restype             = c_int

        self.record_new                     = lib.mbus_record_new
        self.record_new.argtypes            = []
        self.record_new.restype             = mbus_record_p

        self.record_free                    = lib.mbus_record_free
        self.record_free.argtypes           = [mbus_record_p]
        self.record_free.restype            = None

        self.parse_fixed_record             = lib.mbus_parse_fixed_record
        self.parse_fixed_record.argtypes    = [c_byte, c_byte, c_ubyte_p]
        self.parse_fixed_record.restype     = mbus_record_p

        self.parse_variable_record          = lib.mbus_parse_variable_record
        self.parse_variable_record.argtypes = [mbus_data_record_p]
        self.parse_variable_record.restype  = mbus_record_p

        #self.data_fixed_normalize           = lib.mbus_data_fixed_normalize
        #self.data_fixed_normalize.argtypes  = [c_int, c_long, c_char_pp,
        #                                        c_double_p, c_char_pp]
        #self.data_fixed_normalize.restype   = c_int

        #self.data_variable_value_decode     = lib.mbus_data_variable_value_decode
        #self.data_variable_value_decode.argtypes    = [mbus_record_p,
        #                                                c_double_p,
        #                                                c_char_pp, c_int_p]
        #self.data_variable_value_decode.restype     = c_int

        #self.data_vif_unit_normalize     = lib.mbus_data_vif_unit_normalize
        #self.data_vif_unit_normalize.argtypes       = [
        #                c_int, c_double, c_char_pp, c_double_p, c_char_pp]
        #self.data_vif_unit_normalize.restype        = c_int

        #self.data_vib_unit_normalize     = lib.mbus_data_vib_unit_normalize
        #self.data_vib_unit_normalize.argtypes       = [
        #                   mbus_value_information_block_p, c_double,
        #                   c_char_pp, c_double_p, c_char_pp]
        #self.data_vib_unit_normalize.restype        = c_int

        self.data_variable_xml_normalized           = \
                lib.mbus_data_variable_xml_normalized
        self.data_variable_xml_normalized.argtypes  = [
                mbus_value_information_block_p]
        self.data_variable_xml_normalized.restype   = c_char_p

        self.scan_2nd_address_range         = lib.mbus_scan_2nd_address_range
        self.scan_2nd_address_range.argtypes    = [mbus_handle_p, c_int, c_char_p]
        self.scan_2nd_address_range.restype     = c_int

        self.hex2bin                        = lib.mbus_hex2bin
        self.hex2bin.argtypes               = [c_ubyte_p, c_size_t,
                                                c_char_p, c_size_t]
        self.hex2bin.restype                = c_long

        # mbus-protocol.h
        self.manufacturer_id                = lib.mbus_manufacturer_id
        self.manufacturer_id.argtypes       = [c_char_p]
        self.manufacturer_id.restype        = c_int

        self.dump_recv_event                = lib.mbus_dump_recv_event
        self.dump_recv_event.argtypes       = [c_ubyte, c_char_p, c_size_t]
        self.dump_recv_event.restype        = None

        self.dump_send_event                = lib.mbus_dump_send_event
        self.dump_send_event.argtypes       = [c_ubyte, c_char_p, c_size_t]
        self.dump_send_event.restype        = None

        self.data_record_new                = lib.mbus_data_record_new
        self.data_record_new.argtypes       = []
        self.data_record_new.restype        = mbus_data_record_p

        self.data_record_free               = lib.mbus_data_record_free
        self.data_record_free.argtypes      = [mbus_data_record_p]
        self.data_record_free.restypes      = None

        self.data_record_append             = lib.mbus_data_record_append
        self.data_record_append.argtypes    = [mbus_data_variable_p,
                                                mbus_data_record_p]
        self.data_record_append.restypes    = None

        self.frame_new                      = lib.mbus_frame_new
        self.frame_new.argtypes             = []
        self.frame_new.restype              = mbus_frame_p

        self.frame_free                     = lib.mbus_frame_free
        self.frame_free.argtypes            = [mbus_frame_p]
        self.frame_free.restypes            = None

        self.frame_data_new                 = lib.mbus_frame_data_new
        self.frame_data_new.argtypes        = []
        self.frame_data_new.restype         = mbus_frame_data_p

        self.frame_data_free                = lib.mbus_frame_data_free
        self.frame_data_free.argtypes       = [mbus_frame_data_p]
        self.frame_data_free.restypes       = None

        self.frame_calc_checksum            = lib.mbus_frame_calc_checksum
        self.frame_calc_checksum.argtypes   = [mbus_frame_p]
        self.frame_calc_checksum.restypes   = c_int

        self.frame_calc_length              = lib.mbus_frame_calc_length
        self.frame_calc_length.argtypes     = [mbus_frame_p]
        self.frame_calc_length.restypes     = c_int

        self.parse                          = lib.mbus_parse
        self.parse.argtypes                 = [mbus_frame_p, c_ubyte_p,
                                                c_size_t]
        self.parse.restype                  = c_int

        self.data_fixed_parse               = lib.mbus_data_fixed_parse
        self.data_fixed_parse.argtypes      = [mbus_frame_p, mbus_data_fixed_p]
        self.data_fixed_parse.restype       = c_int

        self.data_variable_parse            = lib.mbus_data_variable_parse
        self.data_variable_parse.argtypes   = [mbus_frame_p, mbus_data_variable_p]
        self.data_variable_parse.restype    = c_int

        self.frame_data_parse               = lib.mbus_frame_data_parse
        self.frame_data_parse.argtypes      = [mbus_frame_p, mbus_frame_data_p]
        self.frame_data_parse.restype       = c_int

        self.frame_pack                     = lib.mbus_frame_pack
        self.frame_pack.argtypes            = [mbus_frame_p, c_ubyte_p,
                                                c_size_t]
        self.frame_pack.restype             = c_int

        self.frame_verify                   = lib.mbus_frame_verify
        self.frame_verify.argtypes          = [mbus_frame_p]
        self.frame_verify.restype           = c_int
    
        self.frame_internal_pack            = lib.mbus_frame_internal_pack
        self.frame_internal_pack.argtypes   = [mbus_frame_p, mbus_frame_data_p]
        self.frame_internal_pack.restype    = c_int

        self.data_record_function           = lib.mbus_data_record_function
        self.data_record_function.argtypes  = [mbus_data_record_p]
        self.data_record_function.restype   = c_char_p

        self.data_fixed_function            = lib.mbus_data_fixed_function
        self.data_fixed_function.argtypes   = [c_int]
        self.data_fixed_function.restype    = c_char_p

        self.data_record_storage_number     = lib.mbus_data_record_storage_number
        self.data_record_storage_number.argtypes   = [mbus_data_record_p]
        self.data_record_storage_number.restype    = c_long

        self.data_record_tariff             = lib.mbus_data_record_tariff
        self.data_record_tariff.argtypes    = [mbus_data_record_p]
        self.data_record_tariff.restype     = c_long

        self.data_record_device             = lib.mbus_data_record_device
        self.data_record_device.argtypes    = [mbus_data_record_p]
        self.data_record_device.restype     = c_int

        self.frame_type                     = lib.mbus_frame_type
        self.frame_type.argtypes            = [mbus_frame_p]
        self.frame_type.restype             = c_int

        self.frame_direction                = lib.mbus_frame_direction
        self.frame_direction.argtypes       = [mbus_frame_p]
        self.frame_direction.restype        = c_int

        self.slave_data_get                 = lib.mbus_slave_data_get
        self.slave_data_get.argtypes        = [c_size_t]
        self.slave_data_get.restype         = mbus_slave_data_p

        self.str_xml_encode                 = lib.mbus_str_xml_encode
        self.str_xml_encode.argtypes        = [c_char_p, c_char_p, c_size_t]
        self.str_xml_encode.restype         = None

        #self.data_xml                       = lib.mbus_data_xml
        #self.data_xml.argtypes              = [mbus_frame_data_p]
        #self.data_xml.restype               = c_char_p

        self.data_variable_xml              = lib.mbus_data_variable_xml
        self.data_variable_xml.argtypes     = [mbus_data_variable_p]
        self.data_variable_xml.restype      = c_char_p

        self.data_fixed_xml                 = lib.mbus_data_fixed_xml
        self.data_fixed_xml.argtypes        = [mbus_data_fixed_p]
        self.data_fixed_xml.restype         = c_char_p

        self.data_error_xml                 = lib.mbus_data_error_xml
        self.data_error_xml.argtypes        = [c_int]
        self.data_error_xml.restype         = c_char_p

        self.frame_data_xml                 = lib.mbus_frame_data_xml
        self.frame_data_xml.argtypes        = [mbus_frame_data_p]
        self.frame_data_xml.restype         = c_char_p

        self.data_variable_header_xml       = lib.mbus_data_variable_header_xml
        self.data_variable_header_xml.argtypes  = [mbus_data_variable_header_p]
        self.data_variable_header_xml.restype   = c_char_p

        self.frame_xml                      = lib.mbus_frame_xml
        self.frame_xml.argtypes             = [mbus_frame_p]
        self.frame_xml.restype              = c_char_p

        self.frame_print                    = lib.mbus_frame_print
        self.frame_print.argtypes           = [mbus_frame_p]
        self.frame_print.restype            = c_int

        self.frame_data_print               = lib.mbus_frame_data_print
        self.frame_data_print.argtypes      = [mbus_frame_data_p]
        self.frame_data_print.restype       = c_int

        self.data_fixed_print               = lib.mbus_data_fixed_print
        self.data_fixed_print.argtypes      = [mbus_data_fixed_p]
        self.data_fixed_print.restype       = c_int

        self.data_error_print               = lib.mbus_data_error_print
        self.data_error_print.argtypes      = [c_int]
        self.data_error_print.restype       = c_int

        self.data_variable_header_print     = \
                lib.mbus_data_variable_header_print
        self.data_variable_header_print.argtypes  = [
                mbus_data_variable_header_p]
        self.data_variable_header_print.restype   = c_int

        self.data_variable_print            = lib.mbus_data_variable_print
        self.data_variable_print.argtypes   = [mbus_data_variable_p]
        self.data_variable_print.restype    = c_int

        self.error_str                      = lib.mbus_error_str
        self.error_str.argtypes             = []
        self.error_str.restype              = c_char_p

        self.error_str_set                  = lib.mbus_error_str_set
        self.error_str_set.argtypes         = [c_char_p]
        self.error_str_set.restype          = None

        #self.error_str_reset                = lib.mbus_error_str_reset
        #self.error_str_reset.argtypes       = []
        #self.error_str_reset.restype        = None

        self.parse_set_debug                = lib.mbus_parse_set_debug
        self.parse_set_debug.argtypes       = [c_int]
        self.parse_set_debug.restype        = None

        self.hex_dump                       = lib.mbus_hex_dump
        self.hex_dump.argtypes              = [c_char_p, c_char_p, c_size_t]
        self.hex_dump.restype               = None

        self.data_manufacturer_encode       = lib.mbus_data_manufacturer_encode
        self.data_manufacturer_encode.argtypes  = [c_ubyte_p, c_ubyte_p]
        self.data_manufacturer_encode.restype   = c_int

        self.decode_manufacturer            = lib.mbus_decode_manufacturer
        self.decode_manufacturer.argtypes   = [c_ubyte, c_ubyte]
        self.decode_manufacturer.restype    = c_char_p

        self.data_product_name              = lib.mbus_data_product_name
        self.data_product_name.argtypes     = [mbus_data_variable_header_p]
        self.data_product_name.restype      = c_char_p

        self.data_bcd_encode                = lib.mbus_data_bcd_encode
        self.data_bcd_encode.argtypes       = [c_ubyte_p, c_size_t, c_int]
        self.data_bcd_encode.restype        = c_int

        self.data_int_encode                = lib.mbus_data_int_encode
        self.data_int_encode.argtypes       = [c_ubyte_p, c_size_t, c_int]
        self.data_int_encode.restype        = c_int

        self.data_bcd_decode                = lib.mbus_data_bcd_decode
        self.data_bcd_decode.argtypes       = [c_ubyte_p, c_size_t]
        self.data_bcd_decode.restype        = c_longlong

        self.data_int_decode                = lib.mbus_data_int_decode
        self.data_int_decode.argtypes       = [c_ubyte_p, c_size_t, c_int_p]
        self.data_int_decode.restype        = c_int

        self.data_long_decode               = lib.mbus_data_long_decode
        self.data_long_decode.argtypes      = [c_ubyte_p, c_size_t, c_long_p]
        self.data_long_decode.restype       = c_int

        self.data_long_long_decode          = lib.mbus_data_long_long_decode
        self.data_long_long_decode.argtypes = [c_ubyte_p, c_size_t,
                                                c_longlong_p]
        self.data_long_long_decode.restype  = c_int

        self.data_float_decode              = lib.mbus_data_float_decode
        self.data_float_decode.argtypes     = [c_ubyte_p]
        self.data_float_decode.restype      = c_int

        self.data_tm_decode                 = lib.mbus_data_tm_decode
        self.data_tm_decode.argtypes        = [c_tm_p, c_ubyte_p, c_size_t]
        self.data_tm_decode.restype         = None

        self.data_str_decode                = lib.mbus_data_str_decode
        self.data_str_decode.argtypes       = [c_ubyte_p, c_ubyte_p, c_size_t]
        self.data_str_decode.restype        = None

        self.data_bin_decode                = lib.mbus_data_bin_decode
        self.data_bin_decode.argtypes       = [c_ubyte_p, c_ubyte_p,
                                                c_size_t, c_size_t]
        self.data_bin_decode.restype        = None

        self.data_fixed_medium              = lib.mbus_data_fixed_medium
        self.data_fixed_medium.argtypes     = [mbus_data_fixed_p]
        self.data_fixed_medium.restype      = c_char_p

        self.data_fixed_unit                = lib.mbus_data_fixed_unit
        self.data_fixed_unit.argtypes       = [c_int]
        self.data_fixed_unit.restype        = c_char_p

        self.data_variable_medium_lookup    = \
                lib.mbus_data_variable_medium_lookup
        self.data_variable_medium_lookup.argtypes   = [c_ubyte]
        self.data_variable_medium_lookup.restype    = c_char_p

        #self.data_unit_prefix               = lib.mbus_data_unit_prefix
        #self.data_unit_prefix.argtypes      = [c_int]
        #self.data_unit_prefix.restype       = c_char_p

        self.data_error_lookup              = lib.mbus_data_error_lookup
        self.data_error_lookup.argtypes     = [c_int]
        self.data_error_lookup.restype      = c_char_p

        #self.data_vib_unit_lookup           = lib.mbus_data_vib_unit_lookup
        #self.data_vib_unit_lookup.argtypes  = [c_int]
        #self.data_vib_unit_lookup.restype   = c_char_p

        #self.data_vif_unit_lookup           = lib.mbus_data_vif_unit_lookup
        #self.data_vif_unit_lookup.argtypes  = [c_ubyte]
        #self.data_vif_unit_lookup.restype   = c_char_p

        #self.data_dif_datalength_lookup     = \
        #        lib.mbus_data_dif_datalength_lookup
        #self.data_dif_datalength_lookup.argtypes    = [c_ubyte]
        #self.data_dif_datalength_lookup.restype     = c_ubyte

        self.frame_get_secondary_address    = \
                lib.mbus_frame_get_secondary_address
        self.frame_get_secondary_address.argtypes   = [mbus_frame_p]
        self.frame_get_secondary_address.restype    = c_char_p

        self.frame_select_secondary_pack    = \
                lib.mbus_frame_select_secondary_pack
        self.frame_select_secondary_pack.argtypes   = [mbus_frame_p, c_char_p]
        self.frame_select_secondary_pack.restype    = c_int

        self.is_primary_address             = lib.mbus_is_primary_address
        self.is_primary_address.argtypes    = [c_int]
        self.is_primary_address.restype     = c_int

        self.is_secondary_address           = lib.mbus_is_secondary_address
        self.is_secondary_address.argtypes  = [c_char_p]
        self.is_secondary_address.restype   = c_int

        self.tcp_connect                    = lib.mbus_tcp_connect
        self.tcp_connect.argtypes           = [mbus_handle_p]
        self.tcp_connect.restype            = c_int

        self.tcp_disconnect                 = lib.mbus_tcp_disconnect
        self.tcp_disconnect.argtypes        = [mbus_handle_p]
        self.tcp_disconnect.restype         = c_int

        self.tcp_send_frame                 = lib.mbus_tcp_send_frame
        self.tcp_send_frame.argtypes        = [mbus_handle_p, mbus_frame_p]
        self.tcp_send_frame.restype         = c_int

        self.tcp_recv_frame                 = lib.mbus_tcp_recv_frame
        self.tcp_recv_frame.argtypes        = [mbus_handle_p, mbus_frame_p]
        self.tcp_recv_frame.restype         = c_int

        self.tcp_data_free                  = lib.mbus_tcp_data_free
        self.tcp_data_free.argtypes         = [mbus_handle_p]
        self.tcp_data_free.restype          = None

        self.tcp_set_timeout_set            = lib.mbus_tcp_set_timeout_set
        self.tcp_set_timeout_set.argtypes   = [c_double]
        self.tcp_set_timeout_set.restype    = c_int

        self.serial_connect                 = lib.mbus_serial_connect
        self.serial_connect.argtypes        = [mbus_handle_p]
        self.serial_connect.restype         = c_int

        self.serial_disconnect              = lib.mbus_serial_disconnect
        self.serial_disconnect.argtypes     = [mbus_handle_p]
        self.serial_disconnect.restype      = c_int

        self.serial_send_frame              = lib.mbus_serial_send_frame
        self.serial_send_frame.argtypes     = [mbus_handle_p, mbus_frame_p]
        self.serial_send_frame.restype      = c_int

        self.serial_recv_frame              = lib.mbus_serial_recv_frame
        self.serial_recv_frame.argtypes     = [mbus_handle_p, mbus_frame_p]
        self.serial_recv_frame.restype      = c_int

        self.serial_set_baudrate            = lib.mbus_serial_set_baudrate
        self.serial_set_baudrate.argtypes   = [mbus_handle_p, c_long]
        self.serial_set_baudrate.restype    = c_int

        self.serial_data_free               = lib.mbus_serial_data_free
        self.serial_data_free.argtypes      = [mbus_handle_p]
        self.serial_data_free.restype       = None
