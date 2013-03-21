import sys
sys.path.append('../python-mbus')
import pytest
from mbus import MBus

def test_empty_init():
    with pytest.raises(Exception):
        foo = MBus.MBus()
