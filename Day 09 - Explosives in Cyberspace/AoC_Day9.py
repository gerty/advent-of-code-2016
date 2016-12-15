# Code written by @gerty

# Input from Day 9, Problem 1 & 2 of Advent of Code 2016
# Input files in same directory
# My input: in file Day9input.txt

inputchar = ''
uncompdata = ''


def decompress(inputstring):
    instring = str(inputstring)  # <-- our input string, but in a local variable so we can do with it what we want
    decompstring = ''       # <-- final decompressed string we build up as the answer

    codes = ''             # <-- the tiny string of data inside the '()'
    sniplen = 0         # <-- tracks the length of string to be snipped for copying
    copies = 0          # <-- tracks the number of copies of the copystring needed
    copystring = ''        # <-- the shorter string we load up for copying per the values in '()'

    while len(instring) > 0:
        if '(' in instring:
            decompstring += instring.split('(', 1)[0]  # simple copy of chars until reaching a '('
            instring = instring.split('(', 1)[1]  # remove transferred parts and reassign the rest to instring

        #  Now we either have a string of only characters, or the beginning of a tag to process

        if ')' in instring:
            codes = str(instring.split(')', 1)[0])  # should return us something like '3x2', '1x40', or '0x34'
            print(codes)
            sniplen = int(codes.split('x')[0])  # the length of the copystring is the first number
            copies = int(codes.split('x')[1])   # the number of chars in the copystring is the second number
            copystring = instring.split(')', 1)[1][0:sniplen]  # create the copystring
            for i in range(copies):         # copy the sniplength-long copystring numcopies times
                decompstring += decompress(copystring) # Could it be that I only need to change ONE LINE for part 2???
            instring = instring.split(')', 1)[1]  # remove codes from instring
            instring = instring[len(copystring):]   # also take away the chars that made up the copystring

        # if there are no codes left, dump the rest and empty instring

        if not ('(' in instring):
            decompstring += instring
            instring = ''
    return decompstring   # when instring is empty, return the answer

with open('D9test', 'r') as f:
    rawdata = str(f.read())  # ALERT!! Using "readlines" here adds a character, presuming EOL, making file act up

uncompdata = decompress(rawdata)
print(len(uncompdata))

# My first, unrealistic-looking guess was 107036. Wrong and too high.
# The next result was much more reasonable: 107035. Correct!

# For part two, I first thought that I could just recursively find the decompressed string by changing one line, as
# one can read in my excitement around line 34. Will next attempt to change code to only count and not save the string.
# I mean, what do we do with it anyways? Nothing.
