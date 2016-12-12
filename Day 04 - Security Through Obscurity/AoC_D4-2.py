#!/usr/bin/python
# Code written by @gerty
# 12-7-2016
# This is the first day using Python 3 in the miniconda environment - then switched to just PyCharm

import collections

# Input from Day 4, Problem 2 of Advent of Code (yes, I'm behind!)
# Input files in same directory
# My input: in file D4input.txt

rawdata = []     # <-- all the lines of data
crypt = []       # <-- just the encrypted data
rooms = []       # <-- only the room numbers
checksums = []   # <-- only the checksums
worksum = collections.Counter()
calcsum = ''     # <-- calculated checksum for room
tempsum = []
sectorIDsum = 0    # <-- sum of real room numbers

f = open('D4input.txt', 'r')
rawdata = f.readlines()

for line in range(len(rawdata)):
    crypt.append(rawdata[line].split("-")[:-1])  # <-- Establish crypt with split checksum
    crypt[line] = ''.join(crypt[line])          # <-- (put the string back together)

    rooms.append(rawdata[line].split("[")[0].split("-")[-1])  # <-- Establish rooms with the room number
    checksums.append(rawdata[line].split("[")[1][0:5])        # <-- Establish checksums

    #  Once you have lists of encrypted data for each room, the room number, and the checksum...

    worksum = collections.Counter(crypt[line])  # <-- Load up single use of worksum

#    print(worksum, rooms[line], checksums[line])

    calcsum = ''
    while len(calcsum) < 5:            # <-- While we still have less than 5 chars in our calcsum
        x = worksum.most_common(1)[0][1]     # <-- Find the max occurring number of chars in worksum collection
#        print(x)
        temp = ''                              # <-- Get ready to add somethng to calcsum
        for letter, count in worksum.most_common():   # <-- Looking at all of the remaining entries in worksum
            if count == x:                          # <-- if a letter is one of the top occurring left in the set
                temp += letter                      # <-- then add the letter to our yet-to-be-sorted string
        for count in range(len(temp)):
            worksum.pop(temp[count])  # Remove largest entries from worksum so they don't reappear
        calcsum += ''.join(sorted(temp))  # Add the sorted list of letters with x frequency to calcsum
#        print(calcsum)

    if calcsum[0:5] == checksums[line]:
        sectorIDsum += int(rooms[line])
        answer = ''
        for ch in crypt[line]:
            t1 = int(rooms[line])
            t2 = (ord(ch) - ord('a'))
            letter = chr((t1+t2)%26 + ord('a'))
            answer += letter
        print(answer,rooms[line])

print(sectorIDsum)

# First attempt returns 6367, and was too low
# Second attempt yielded 361724, and ... was correct!

# The north pole objects are stored in 482 - output file saved.
