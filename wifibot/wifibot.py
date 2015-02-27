#!/usr/bin/env python

import serial

s = serial.Serial('/dev/ttyUSB0', baudrate=19200)

addr = 0xA4
speed = 84

d = [0x55, addr, 0x00, 0x01, speed]

w = ''.join([chr(x) for x in d])
s.write(w)

