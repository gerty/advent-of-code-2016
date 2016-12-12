# Code written by @gerty

# Input from Day 7, Problem 2 of Advent of Code 2016
# Input files in same directory
# My input: in file D7input.txt

import collections
answer = 0


def isThisABA(clip):  # A function to look at 3 characters for the match
    if len(clip) != 3:  # Error-check for a wrongly sized string
        return False
    if clip[0] == clip[1]:  # first catch the case where all might be the same
        return False
    if clip[0] + clip[1] == clip[2] + clip [1]:  # then check for the true ABA case
        return True
    else:
        return False

def searchLineForABA(target):
    ABA = collections.Counter()  # Initialize our collection of ABAs
    BABmatch = False

    # Let's go through this string two separate times - first to find the ABAs, then to match BABs
    ch = 0
    while ch < len(line) - 3:  # (no point in starting further than 3 from end)
        if line[ch] == '[':
            while line[ch] != ']' and ch < len(line):
                ch += 1       # just skip over the bracketed parts
        if isThisABA(line[ch:ch + 3]):
            ABA[line[ch:ch + 3]] += 1  # hold on to the ABA by placing it in a collection
        ch += 1

    ch = 0
    while ch < len(line) - 3:  # (no point in starting further than 3 from end)
        if line[ch] == '[':
            while line[ch] != ']' and ch < len(line) - 3:  # Search until end of brackets, checking for EOL
                if isThisABA(line[ch:ch + 3]):
                    if ABA[line[ch+1] + line[ch] + line[ch+1]] != 0:  # Check the ABA collection for this BAB inside []
                        BABmatch = True
                        print(line[ch:ch + 3])
                ch += 1
        ch += 1

    return BABmatch  # only return True if found ABBA without early escape from def

with open('D7input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    if searchLineForABA(line):
        answer += 1

print(answer)


# First attempt: 231
