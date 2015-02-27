#!/usr/bin/env python

from pylab import *
import random as rnd

from math import *

waypoints = [(0,0), (0,10), (4,0), (4,10), (0,0)]

rn = 0.02
onx = 0
ony = 0

rd = 0.15
odx = 0.2
ody = 0.9
rg = 0.05
ogx = 3.1
ogy = 1.8
dg = 0.1

pgg = 0.99
pgd = 0.97

ggm = 0.5
dgm = 0.5

speed = 1
rate = 5

rpx, rpy = [], []
dpx, dpy = [], []
gpx, gpy = [], []

def random():
    return 2 * rnd.random() - 1

for i in range(len(waypoints) - 1):
    s = waypoints[i]
    e = waypoints[i+1]
    d = sqrt((s[0]-e[0])**2 + (s[1]-e[1])**2)
    pn = int(rate * d / speed)

    for p in range(pn):
        r = float(p) / pn;

        pbx = s[0] * (1 - r) + e[0] * r
        pby = s[1] * (1 - r) + e[1] * r

        ggx = ggm * random() if random() > pgg else 0
        ggy = ggm * random() if random() > pgg else 0

        dgx = dgm * random() if random() > pgd else 0
        dgy = dgm * random() if random() > pgd else 0

        rpx.append(pbx + random() * rn + onx)
        rpy.append(pby + random() * rn + ony)
        dpx.append(pbx + random() * rd + odx + dgx)
        dpy.append(pby + random() * rd + ody + dgy)
        gpx.append(pbx + random() * rg + ogx + ggx)
        gpy.append(pby + random() * rg + ogy + ggy)

        odx += random() * 0.01
        ody += random() * 0.02

        ogx += random() * 0.02
        ogy += random() * 0.02

        onx += random() * 0.01
        ony += random() * 0.01

plot(rpx, rpy, '-', label="RTK")
plot(dpx, dpy, 'x-', c='g', label="DGPS")
plot(gpx, gpy, '.-', c='r', label="Uncorrected")
legend(loc=4)
show()

