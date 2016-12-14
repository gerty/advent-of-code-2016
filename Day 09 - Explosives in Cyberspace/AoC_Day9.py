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
    snip = 0         # <-- tracks the length of string to be snipped for copying
    copies = 0          # <-- tracks the number of copies of the copystring needed
    copystring = ''        # <-- the shorter string we load up for copying per the values in '()'

    if '(' in instring:
        decompstring += instring.split('(', 1)[0]  # copy chars exact until reaching a '(', then stop
    if '(' in instring:
        instring = instring.split('(', 1)[1]  # remove the easily transferred parts and reassign the rest to instring

    while len(instring) > 0:                    # always start here with a code ready without '(', or empty string
        codes = instring.split(')',1)[0]  # should return us something like '3x2', '1x40', or '0x34'
        print(codes)
        snip = int(codes.split('x')[0])  # the length of the copystring is the first number
        copies = int(codes.split('x')[1])   # the number of chars in the copystring is the second number
        copystring = instring.split(')',1)[1][0:snip]  # create the copystring
        for i in range(copies):         # copy the sniplength-long copystring numcopies times
            decompstring += copystring
        instring = instring.split(')',1)[1]  # remove codes from instring
        instring = instring[len(copystring):]   # also take away the chars that made up the copystring
        if '(' in instring:
            decompstring += instring.split('(', 1)[0]  # copy chars exact until reaching a '(', then stop
        else:
            decompstring += instring   # if there are no codes left, dump the rest and empty instring
            instring = ''
        if '(' in instring:
            instring = instring.split('(', 1)[1]  # remove the easily transferred parts, reassign the rest to instring
    return(decompstring)   # when instring is empty, return the answer

uncompdata = decompress(rawdata[0])
print(len(uncompdata))

# My first, unrealistic-looking guess was 107036. Wrong and too high.
# The next result was much more reasonable: 107035. Correct!
