import sys
sys.path.append('../python-mbus')
import pytest
from mbus import MBus


@pytest.fixture
def mbus_tcp():
    return MBus.MBus(host="127.0.0.1")


def test_connect(mbus_tcp):
    mbus_tcp.connect()
