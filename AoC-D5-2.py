# Code written by @gerty
# 12-8-2016

import hashlib

# Input from Day 5, Problem 2 of Advent of Code
# Input files in same directory
# My input: in file D4input.txt

D5input = b'reyedfim'
D5test = b'abc'
answer = ['_', '_', '_', '_', '_', '_', '_', '_']
h = hashlib.md5()
i = 0
ans = 0
print(i, answer)

while ans < 8:
    h = hashlib.md5()
    h.update(D5input+str(i).encode('utf-8'))
    thishash = h.hexdigest()
    if str(thishash)[0:5] == '00000':
        if thishash[5] < '8':
            if answer[int(thishash[5])] == '_':
                answer[int(thishash[5])] = thishash[6]
                ans += 1
        print(i, answer, thishash)
    i += 1

print(answer)

# Worked with the test numbers to find 05ace8e3
# First real solution came back as '863dde27' - yes! It's a winner!!
