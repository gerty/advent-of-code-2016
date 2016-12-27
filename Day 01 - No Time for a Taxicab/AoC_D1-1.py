# Code written by @gerty
# 12-2-2016

import csv

# Input from Day 1, Problem 1 of Advent of Code
# Input files in same directory
# input = "R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"
#testinput1 = "R2, L3"
#testans1 = 2
#testinput2 = "R2, R2, R2"
#testans2 = 2
#testinput3 = "R5, L5, R5, R3"
#testans3 = 12

xaxis = 0
yaxis = 0
mydirection = 'N'

def turn (thisway,currentDirection) :
	if currentDirection == 'N':
		if thisway == "R": return('E')
		if thisway == "L": return('W')
	if currentDirection == 'E':
		if thisway == "R": return('S')
		if thisway == "L": return('N')
	if currentDirection == 'S':
		if thisway == "R": return('W')
		if thisway == "L": return('E')
	if currentDirection == 'W':
		if thisway == "R": return('N')
		if thisway == "L": return('S')
	else: return 'ERROR'
	

with open('D1P1input.csv', 'r') as f:
    reader = csv.reader(f)
    for list in reader:
        gohere = list
gohere[0] = ' ' + gohere[0]
for x in gohere:
	print ('Facing', mydirection, '(about to turn', x[1], 'and go', x[2:], 'spaces)')
	mydirection = turn(x[1],mydirection)
	if mydirection == 'N':	
		yaxis = yaxis + int(x[2:])
	if mydirection == 'E':	
		xaxis = xaxis + int(x[2:])
	if mydirection == 'S':	
		yaxis = yaxis - int(x[2:])
	if mydirection == 'W':	
		xaxis = xaxis - int(x[2:])
print ('Finished at location: ', xaxis, ',', yaxis)
print (abs(xaxis) + abs(yaxis)), 'away from starting point.'		


