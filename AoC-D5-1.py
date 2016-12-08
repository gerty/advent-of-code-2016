# Code written by @gerty
# 12-4-2016

import hashlib

# Input from Day 5, Problem 1 of Advent of Code
# Input files in same directory
# My input: in file D4input.txt

D5input = b'reyedfim'
D5test = b'abc'
answer = '________xx'
h = hashlib.md5()
i = 0

while len(answer) < 8:
    h = hashlib.md5()
    h.update(D5input+str(i).encode('utf-8'))
    thishash = h.hexdigest()
    if str(thishash)[0:5] == '00000':
        answer += h.hexdigest()[5]
        print(i, answer, thishash)
    i += 1

print(answer)

# Got this one on the first try: f97c354d
# Learned a lot about hashing from https://docs.python.org/3/library/hashlib.html and other sites...
