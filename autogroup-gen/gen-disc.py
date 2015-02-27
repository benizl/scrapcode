#!/usr/bin/env python

eo = [
	"Even Weeks",
	"Odd Weeks"
]

disc = [
	"Discipline - Materials and Manufacturing",
	"Discipline - Electronics and Telecommunications",
	"Discipline - Mechatronics",
	"Discipline - Rewable Energy/ Sustainability",
	"Discipline - Software Systems/ Computer Science"
]

with open("dgroups.csv", "w") as f:
	f.write("groupname\n")

	for d in disc:
		for e in eo:
			f.write(d)
			f.write(": ")
			f.write(e)
			f.write("\n")

