#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Copyright (C) 2012, Robert Johansson <rob@raditex.nu>, Raditex Control AB
# All rights reserved.
# ------------------------------------------------------------------------------

"""
mbus test: send a request frame and receive and parse the reply
"""

from mbus import *

debug = True
address = 1

mbus = MBus("localhost", 1200)

if debug:
    print("mbus = ", mbus)

mbus.connect()

if debug:
    print("mbus = ", mbus)

mbus.send_request_frame(address)

reply = mbus.recv_frame()

if debug:
    print("reply =", reply)

reply_data = mbus.frame_data_parse(reply)

if debug:
    print("reply_data =", reply_data)

xml_buff = mbus.frame_data_xml(reply_data)

print("xml_buff =", xml_buff)
