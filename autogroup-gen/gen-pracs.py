#!/usr/bin/env python

groups = [
	"Prac 1 - Tuesday 11am",
	"Prac 2 - Tuesday 1pm",
	"Prac 3 - Wednesday 9am",
	"Prac 4 - Wednesday 11am",
	"Prac 5 - Wednesday 2pm",
	"Prac 6 - Thursday 9am",
	"Prac 7 - Thursday 11am",
	"Prac 8 - Thursday 3pm",
	"Prac 9 - Friday 11am",
	"Prac 10 - Friday 1pm",
]

disc = [
	"Materials and Manufacturing",
	"Electronics and Telecommunications",
	"Mechatronics",
	"Rewable Energy/ Sustainability",
	"Software Systems/ Computer Science"
]

with open("groups.csv", "w") as f:
	f.write("groupname\n")

	for g in groups:
		for d in disc:
			f.write(g)
			f.write(": ")
			f.write(d)
			f.write("\n")

