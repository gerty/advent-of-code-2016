# Code written by @gerty
# 12-3-2016

import csv, string

# Input from Day 3, Problem 1 of Advent of Code
# Input files in same directory
# My input:

r0 = [0,0,0,]
r1 = [0,0,0,]
r2 = [0,0,0,]

# First guess on this second run was 982, but since that was the exact answer last
# time, I'm assuming I have the columns and rows messed up again. Didn't submit.
# Ugh. Actually I was still executing the old file.
# First 'real' guess is: 

def possibleTriangle (a, b, c) :
	if (a+b<=c) or (b+c<=a) or (a+c<=b) : return False
	else : return True;

tri = 0;

with open('D3input.txt', 'rb') as f:
    tridata = csv.reader(f)
    count = 0
    for row in tridata : # for each three rows
		if count == 0 : r0 = row[0].split()
		if count == 1 : r1 = row[0].split()
		if count == 2 : r2 = row[0].split()
		if (count < 2) : count = count + 1
	   	else : 
	   	# Checking first column
	   		if possibleTriangle(int(r0[0]),int(r1[0]),int(r2[0])) : 
				tri = tri + 1
				print int(r0[0]),int(r1[0]),int(r2[0])
		# Checking second column
			if possibleTriangle(int(r0[1]),int(r1[1]),int(r2[1])) : 
				tri = tri + 1
				print int(r0[1]),int(r1[1]),int(r2[1])
		# Checking third column
			if possibleTriangle(int(r0[2]),int(r1[2]),int(r2[2])) : 
				tri = tri + 1
				print int(r0[2]),int(r1[2]),int(r2[2])
		# Reset count
			count = 0
print tri


