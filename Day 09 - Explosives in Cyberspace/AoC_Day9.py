# Code written by @gerty

# Input from Day 9, Problem 1 & 2 of Advent of Code 2016
# Input files in same directory
# My input: in file Day9input.txt

inputchar = ''
uncompdata = ''

with open('Day9input.txt', 'r') as f:
    rawdata = f.readlines()

def decompress(inputstring):
    instring = inputstring  # <-- our input string, but in a local variable so we can do with it what we want
    decompstring = ''       # <-- final decompressed string we build up as the answer
    codes = ''             # <-- the tiny string of data inside the '()'
    sniplength = 0         # <-- tracks the length of string to be snipped for copying
    numcopies = 0          # <-- tracks the number of copies of the copystring needed
    copystring = ''        # <-- the shorter string we load up for copying per the values in '()'
    index = 0
    while len(instring) > 0:
        decompstring += instring.split('(')[0]  # simply transfer the string until reaching a '('
        codes = instring.split('()')[1]  # should return us something like '3x2', '1x40', or '0x34' ** out of range **
        sniplength = int(codes.split('x')[0])  # the length of the copystring is the first number
        numcopies = int(codes.split('x')[1])   # the number of chars in the copystring is the second number
        copystring = instring.split(')')[1][0:sniplength]  # create the copystring ** removing later-appearing ()s!! **
        for i in range(numcopies):         # copy the sniplength-long copystring numcopies times
            decompstring += copystring
        instring = ''.join(instring.split(')')[1:])  # remove the codes from instring ** but not all of them!! **
        instring = instring[len(copystring):]   # also take away the chars that made up the copystring
    return(tempstring1)   # when instring is empty, return the answer

uncompdata = decompress(rawdata[0])
print(uncompdata)
