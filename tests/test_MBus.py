import sys
sys.path.append('../python-mbus')
import pytest
from mbus import MBus

def test_empty_init():
    with pytest.raises(Exception):
        foo = MBus.MBus()

def test_device_null():
    with pytest.raises(TypeError):
        foo = MBus.MBus('/dev/null')

def test_device_nonexistent():
    with pytest.raises(FileNotFoundError):
        foo = MBus.MBus('/dev/idonotexist')

#def test_device_ttyUSB0():
#    with pytest.raises(TypeError):
#        foo = MBus.MBus('/dev/ttyUSB0')
# device=None, host=None, port=8888

def test_device_and_host():
    with pytest.raises(BaseException):
        foo = MBus.MBus('/dev/null','127.0.0.1')
