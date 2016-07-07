#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'ByStudent'
def patch_pak():
   file_r = open("libCheck.so", "rb")
   content = file_r.read()
   file_r.close()
   data = ""
   begin_pos = 0x0000243C&0xfffffffe
   end_pos = 0x3E68
   pos = begin_pos
   while pos != end_pos:
      data += chr(ord(content[pos])^0xAA)
      pos += 1
   file_w = open("libCheck-patch.so", "wb")
   file_w.write(content[:begin_pos]+data+content[end_pos:])
   file_w.close()
def decode():
   name = "hawking"
   v42 = [0]*17
   v42[1] = 0xE6;
   v42[2] = 0xE6;
   v42[4] = -111;
   v42[6] = -110;
   v42[10] = -111;
   v42[12] = -110;
   v42[14] = -110;
   v42[3] = -40;
   v42[5] = -109;
   v42[8] = -109;
   v42[11] = -107;
   v42[15] = -105;
   v42[7] = -106;
   v42[9] = -117;
   v42[13] = -112;
   v42[16] = -61;
   v42[0] = -28;
   for item in v42:
      name += chr(((item - 8)^0xbb)&0xff)
   print [hex(ord(c)) for c in name]
   new_name = ""
   for item in name[:-1]:
      new_name += chr(((ord(item)^0x22)+0x78)&0xff)
   print [hex(ord(c)) for c in new_name]
   print new_name.encode("hex")
decode()
