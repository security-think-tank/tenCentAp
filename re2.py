#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
str11 = "ac79e91746eb589e"
str1 = ""
for item in str11:
   if item >= 'a' and item <= 'f':
      str1 += chr(ord(item)-ord('a')+ord('0')+10)
   else:
      str1 += item
#str1 = str11
str11 = str1
str1 = ""
for item in str11:
   str1 += hex(ord(item))[2:].strip("L")
print [hex(ord(c)) for c in str1]
str1_changed = ""
for i in range(len(str1)/2):
   str1_changed += hex(int(str1[2*i:2*i+2], 16)^0x86)[2:].strip("L")
print str1_changed
exit(0)
import struct
def p(val):
   return struct.pack("I", val)
def u(val):
   return struct.unpack("I", val)[0]
file_r = open(R"C:\Users\Administrator\Documents\Tencent Files\420064976\FileRecv\re\re\Reverse2\re2\KeyGenMe_00404000.mem", 'rb')
content = file_r.read()
file_r.close()
data_404150 = content[0x150:0x550]
file_r = open(R"C:\Users\Administrator\Documents\Tencent Files\420064976\FileRecv\re\re\Reverse2\re2\KeyGenMe_00402000.mem", 'rb')
content = file_r.read()
file_r.close()
data_402010 = content[0x10:0xAC0]
dword_404150 = []
for i in range(len(data_404150)/4):
   dword_404150.append(u(data_404150[4*i:4*i+4]))
#print [hex(c) for c in dword_404150]
#print [hex(ord(c)) for c in data_402010]
def sub_4015A0(buff, size):
   global data_402010
   i = 0
   changed_data_402010 = []
   val = p(u(buff) ^ 0xD9EE7A1B)
   #print [hex(ord(c)) for c in val]
   if size > 0:
      while i < size:
         changed_data_402010.append(chr(ord(data_402010[i])^ord(val[i&3])))
         #print hex(ord(changed_data_402010[i]))
         #raw_input(":")
         i += 1
   return changed_data_402010
def sub_401550(a1, changed_data_402010, size):
   global dword_404150
   i = 0
   i_ptr = ~a1
   while i < size:
      i_ptr = (dword_404150[(i_ptr&0xff)^ord(changed_data_402010[i])]^((i_ptr>>8)&0xffffff))&0xffffffff
      #print hex(i_ptr)
      #raw_input(":")
      i += 1
   return (~i_ptr)&0xffffffff
def try_buff(buff):
   changed_data_402010 = sub_4015A0(buff, 0xAB0)
   #print [hex(ord(c)) for c in changed_data_402010]
   return sub_401550(0, changed_data_402010, 0xAB0)
def bruce_val():
   for i in range(256):
      for j in range(256):
         for k in range(256):
            for l in range(256):
               if try_buff(chr(i)+chr(j)+chr(k)+chr(l)) == 0xAFFE390F:
                  print "get it:",
                  print chr(i)+chr(j)+chr(k)+chr(l)
                  return
str11 = "ac79e91746eb589e"
str1 = ""
for item in str11:
   if item >= 'a' and item <= 'f':
      str1 += chr(ord(item)-ord('a')+ord('0')+10)
   else:
      str1 += item
print str1
str1_changed = ""
for i in range(len(str1)/2):
   str1_changed += hex((ord(str1[i])*10+ord(str1[i+1]))^0x86)[2:].strip("L")
print str1_changed
exit(0)
print hex(try_buff("1234"))

import string
alpha_bet = string.printable
print [hex(ord(c)) for c in alpha_bet]
exit(0)
def bruce_val2():
   for i in alpha_bet:
      for j in alpha_bet:
         print i, j
         for k in alpha_bet:
            for l in alpha_bet:
               if try_buff(i+j+k+l) == 0xAFFE390F:
                  print "get it:",
                  print i+j+k+l
                  return
#bruce_val2()
"""
dword_402010 = []
for i in range(len(data_402010)/4):
   dword_402010.append(u(data_402010[4*i:4*i+4]))
print [hex(c) for c in dword_404150]
print [hex(c) for c in dword_402010]
"""
exit(0)
size = 0xAB0
index = size
i_ptr = 0xAFFE390F
i_ptr = ~i_ptr
while index > 0:
   index -= 1
   print i_ptr
