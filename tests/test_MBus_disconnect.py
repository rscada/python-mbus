import sys
sys.path.append('../python-mbus')
import pytest
from mbus import MBus


@pytest.fixture
def mbus_tcp_connected():
    tmp = MBus.MBus(libpath="/usr/local/lib/libmbus.so", host="127.0.0.1")
    return tmp.connect()


def test_connect(mbus_tcp_connected):
    mbus_tcp_connected.disconnect()
