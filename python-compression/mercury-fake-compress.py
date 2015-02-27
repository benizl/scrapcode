#!/usr/bin/env python

import zlib, bz2
import backports.lzma as lzma
import time
import random
import math
import bitstream
from numpy import uint8

from operator import add

width = 640
height = 480
bpp = 1

waveforms = 16
outframe = 100

def create_packed():
	b = bitstream.BitStream()
	d = create_composite()

	while len(d) % 8:
		d.append(0)

	b.write(d, bool)

	bts = len(d) / 8
	return b.read(uint8, bts)

def create_packed_random():
	b = bitstream.BitStream()
	d = create_random()

	while len(d) % 8:
		d.append(0)

	b.write(d, bool)

	bts = len(d) / 8

	return b.read(uint8, bts)


def create_composite():
	d = [0] * width * height

	for i in range(waveforms):
		d = map(add, d, create_frame())

	return [min(v, 2**bpp - 1) for v in d]


def create_frame():
	d = [[0 for i in range(width)] for i in range(height)]

	# Sine wave, 20% noise, half-range height, 2 periods in frame
	for i in range(width):
		x = 16 * 2 * math.pi * i / width
		y = math.sin(x) + 0.2 * random.random()

		v = int((y + 2) * height / 4)

		d[v][i] = random.randrange(1,2**bpp - 1) if bpp > 1 else 1

	return [i for sl in d for i in sl]

def _rnd_pixel():
	return (random.randrange(1, 2**bpp - 1) if bpp > 1 else 1) if random.random() < 0.2 else 0

def create_random():
	return [ _rnd_pixel() for x in range(width*height)]

def run_test(d):
	for i in range(0,10):
		s = time.time()
		r = zlib.compress(d, i)
		e = time.time()

		print("ZLib {}: {} {} ({}%)".format(i, e-s, len(r), 100.0*len(d)/len(r)))

	for i in range(1,10):
		s = time.time()
		r = bz2.compress(d, i)
		e = time.time()

		print("BZ2 {}: {} {} ({}%)".format(i, e-s, len(r), 100.0*len(d)/len(r)))

	for i in range(1,10):
		f = [{"id":lzma.FILTER_LZMA2, "preset": i}]
		c = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=f)
		s = time.time()
		r = c.compress(d)
		r += c.flush()
		e = time.time()

		print("LZMA {}: {} {} ({}%)".format(i, e-s, len(r), 100.0*len(d)/len(r)))

	for i in range(1,10):
		f = [{"id":lzma.FILTER_DELTA}, {"id":lzma.FILTER_LZMA2, "preset": i}]
		c = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=f)
		s = time.time()
		r = c.compress(d)
		r += c.flush()
		e = time.time()

		print("LZMA-D {}: {} {} ({}%)".format(i, e-s, len(r), 100.0*len(d)/len(r)))

print "Random"
#run_test("".join([chr(i) for i in create_random()]))

print "Frame"
#run_test("".join([chr(i) for i in create_frame()]))

print "Composite"
#run_test("".join([chr(i) for i in create_composite()]))

print "Packed"
#run_test("".join([chr(i) for i in create_packed()]))


print "Packed Random"
run_test("".join([chr(i) for i in create_packed_random()]))


exit()

with open("comp.raw", "w") as f:
	for i in range(outframe):
		f.write("".join([chr(i) for i in create_composite()]))

with open("packed.raw", "w") as f:
	for i in range(outframe):
		f.write("".join([chr(i) for i in create_packed()]))
