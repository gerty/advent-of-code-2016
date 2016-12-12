# Code written by @gerty

# Input from Day 6, Problem 1 & 2 of Advent of Code 2016
# Input files in same directory
# My input: in file D6input.txt

import collections

answer = ''
answer2 = ''
columns = []
for i in range(8):
    columns.append(collections.Counter()) # Keep track of the columns in a collection that we can tally

with open('D6input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    for ch in range(len(line)-1): # back off one to allow for the \n"
        columns[ch][line[ch]] += 1

for ch in range(8): # allow for the \n"
    answer += str(columns[ch].most_common(1)[0][0]) # thx to: https://docs.python.org/3/library/collections.html
    answer2 += str(columns[ch].most_common()[:-2:-1][0][0]) # thx to: https://docs.python.org/3/library/collections.html
print(answer, answer2)


