# Code written by @gerty

# Input from Day 9, Problem 1 & 2 of Advent of Code 2016
# Input files in same directory
# My input: in file Day9input.txt

inputchar = ''
uncompdata = ''

with open('Day9input.txt', 'r') as f:
    rawdata = f.readlines()

def decompress(inputstring):
    tempstring1 = ''
    incopymode = False
    ministring = ''
    for ch in inputstring:
        tempstring1 += ch
    # parse the string until reaching a '('
    # go into copy mode and read the numbers by re-splitting at the x and the ')'
    # use the numbers to count and copy into ministring
    # exit copymode and continue copying 1:1 and look for the next '('
    # until we're done with the whole lot
    # then,
    return(tempstring1)

uncompdata = decompress(rawdata[0])
print(uncompdata)
