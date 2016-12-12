# Code written by @gerty
# 12-3-2016

import csv, string

# Input from Day 3, Problem 1 of Advent of Code
# Input files in same directory
# My input:

r = [0,0,0]

# First guess, 920, was wrong and too low. I was counting impossible tris
# Next guess, 982, was correct!!

def possibleTriangle (a, b, c) :
	if (a+b<=c) or (b+c<=a) or (a+c<=b) : return False
	else : return True;

tri = 0;

with open('D3input.txt', 'rb') as f:
    tridata = csv.reader(f)
    for row in tridata : # for each row
		r = row[0].split()
	   	if possibleTriangle(int(r[0]),int(r[1]),int(r[2])) : 
			tri = tri + 1
			print int(r[0]),int(r[1]),int(r[2])
print tri


