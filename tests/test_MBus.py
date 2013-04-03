import sys
sys.path.append('../python-mbus')
import pytest
from mbus import MBus


def test_empty_init():
    with pytest.raises(BaseException):
        foo = MBus.MBus()


def test_invalid_argument():
    with pytest.raises(TypeError):
        foo = MBus.MBus(foo='bar')


def test_device_null():
    with pytest.raises(TypeError):
        foo = MBus.MBus(device='/dev/null')


def test_device_nonexistent():
    with pytest.raises(FileNotFoundError):
        foo = MBus.MBus(device='/dev/idonotexist')


#def test_device_ttyUSB0():
#    with pytest.raises(TypeError):
#        foo = MBus.MBus(device='/dev/ttyUSB0')
# device=None, host=None, port=8888


def test_device_and_host():
    with pytest.raises(BaseException):
        foo = MBus.MBus(device='/dev/null', host='127.0.0.1')


def test_port():
    foo = MBus.MBus(host="127.0.0.1", port=1234)


def test_port_too_low():
    with pytest.raises(ValueError):
        MBus.MBus(host="127.0.0.1", port=-1)


def test_port_too_high():
    with pytest.raises(ValueError):
        MBus.MBus(host="127.0.0.1", port=77777)


def test_port_float():
    with pytest.raises(TypeError):
        MBus.MBus(host="127.0.0.1", port=2.3)


def test_port_string():
    with pytest.raises(TypeError):
        MBus.MBus(host="127.0.0.1", port="123")


def test_libpath_empty():
    with pytest.raises(OSError):
        foo = MBus.MBus(libpath='')


def test_libpath_shared_object_only():
    with pytest.raises(OSError):
        foo = MBus.MBus(libpath='libmbus.so')


def test_libpath_shared_object_path():
    foo = MBus.MBus(libpath="/usr/local/lib/libmbus.so", host="127.0.0.1")
