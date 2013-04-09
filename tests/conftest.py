import pytest


# get path to serial device from pytest.ini
def pytest_addoption(parser):
    parser.addini("serialdevice", "path to serial device for testing")
