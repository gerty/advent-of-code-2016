# Code written by @gerty
# 12-2-2016
# Complete on 12-2


import csv

# Input from Day 1, Problem 2 of Advent of Code
# Input files in same directory
# input = "R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1"
# Answer from previous problem was 287
# This answer comes out as 133

xaxis = 0
yaxis = 0
mydirection = 'N'
grid = []
walk = 0

for row in range(1000):
	grid.append([])
	for column in range(1000):
		grid[row].append(False)

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
	

with open('D1P1input.csv', 'rb') as f:
    reader = csv.reader(f)
    for list in reader:
        gohere = list
gohere[0] = ' ' + gohere[0] #needed to fix leading space on first entry for some reason
for x in gohere:
#	print 'Facing', mydirection, '(about to turn', x[1], 'and go', x[2:], 'spaces)'
	mydirection = turn(x[1],mydirection)
	if mydirection == 'N':	
		walk = 0
		while walk < int(x[2:]):
			yaxis = yaxis + 1
			if grid[yaxis+500][xaxis+500]:
				print 'Been here! (', xaxis, ',', yaxis, ')'
				print (abs(xaxis) + abs(yaxis)), 'away from starting point!'
			grid[yaxis+500][xaxis+500] = True
			walk = walk + 1
	if mydirection == 'E':	
		walk = 0
		while walk < int(x[2:]):
			xaxis = xaxis + 1
			if grid[yaxis+500][xaxis+500]:
				print 'Been here! (', xaxis, ',', yaxis, ')'
				print (abs(xaxis) + abs(yaxis)), 'away from starting point!'
			grid[yaxis+500][xaxis+500] = True
			walk = walk + 1		
#		xaxis = xaxis + int(x[2:])
	if mydirection == 'S':	
		walk = 0
		while walk < int(x[2:]):
			yaxis = yaxis - 1
			if grid[yaxis+500][xaxis+500]:
				print 'Been here! (', xaxis, ',', yaxis, ')'
				print (abs(xaxis) + abs(yaxis)), 'away from starting point!'
			grid[yaxis+500][xaxis+500] = True
			walk = walk + 1
#			yaxis = yaxis - int(x[2:])
	if mydirection == 'W':	
		walk = 0
		while walk < int(x[2:]):
			xaxis = xaxis - 1
			if grid[yaxis+500][xaxis+500]:
				print 'Been here! (', xaxis, ',', yaxis, ')'
				print (abs(xaxis) + abs(yaxis)), 'away from starting point!'
			grid[yaxis+500][xaxis+500] = True
			walk = walk + 1
#			xaxis = xaxis - int(x[2:])
print 'Finished at location: ', xaxis, ',', yaxis
print (abs(xaxis) + abs(yaxis)), 'away from starting point.'


