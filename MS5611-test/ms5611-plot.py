#!/usr/bin/env python

from pylab import *

import sys

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
oldt2 = 0
oldt3 = 0
i = 0
oldi = 0

with open(sys.argv[1], 'r') as f:
	for l in f:
		i += 1
		t1, t2, t3, t4, t5 = l.split()
		c1.append(t1)
		c2.append(t2)
		c3.append(t3)
		c4.append(t4)
		c5.append(t5)
		t2 = int(t2)
		t3 = int(t3)
		if abs(t2 - oldt2) > 10000:# or abs(t3 - oldt3) > 10000:
			print("{} {} {} {} {} {} {}".format(i - oldi, t2, oldt2, t3, oldt3, t2-oldt2, t3-oldt3))
			oldi = i

		oldt2 = t2
		oldt3 = t3

plot(c2)
plot(c3)
figure()
plot(c4)
figure()
plot(c5)
show()
