# Code written by @gerty

# Input from Day 9, Problem 1 & 2 of Advent of Code 2016
# Input files in same directory
# My input: in file Day9input.txt

inputchar = ''
uncompdata = []


def decompress(inputstring):
    instring = str(inputstring)  # <-- our input string, but in a local variable so we can do with it what we want
    decompstring = ''       # <-- final decompressed string we build up as the answer
    decompstringlen = 0

    codes = ''             # <-- the tiny string of data inside the '()'
    sniplen = 0         # <-- tracks the length of string to be snipped for copying
    copies = 0          # <-- tracks the number of copies of the copystring needed
    copystring = ''        # <-- the shorter string we load up for copying per the values in '()'

    if not ('(' in instring):
        return(len(instring)) # Get out ASAP if we're at the end of a recursive branch

    while len(instring) > 0:
        if '(' in instring:
            decompstringlen += len(instring.split('(', 1)[0])  # simple copy of chars until reaching a '('
            instring = instring.split('(', 1)[1]  # remove transferred parts and reassign the rest to instring

        #  Now we either have a string of only characters, or the beginning of a tag to process

        if ')' in instring:
            codes = str(instring.split(')', 1)[0])  # should return us something like '3x2', '1x40', or '0x34'
            sniplen = int(codes.split('x')[0])  # the length of the copystring is the first number
            copies = int(codes.split('x')[1])   # the number of chars in the copystring is the second number
            copystring = instring.split(')', 1)[1][0:sniplen]  # create the copystring
            for i in range(copies):         # copy the sniplength-long copystring numcopies times
                decompstringlen += decompress(copystring) # Could it be that I only need to change ONE LINE for part 2?
            instring = instring.split(')', 1)[1]  # remove codes from instring
            instring = instring[len(copystring):]   # also take away the chars that made up the copystring

        # if there are no codes left, dump the rest and empty instring

        if not ('(' in instring):
            decompstringlen += len(instring)
            instring = ''
    return decompstringlen   # when instring is empty, return the answer

with open('Day9input.txt', 'r') as f:
    rawdata = str(f.read())  # ALERT!! Using "readlines" here adds a character, presuming EOL, making file act up

print (decompress(rawdata))

# My first, unrealistic-looking guess was 107036. Wrong and too high.
# The next result was much more reasonable: 107035. Correct!

#  For part two, I first thought that I could just recursively find the decompressed string by changing one line, as
#  one can read in my excitement around line 34. Will next attempt to change code to only count and not save the string.
#  I mean, what do we do with it anyways? Nothing.

#  OK, so the attempt will be to pass an integer back from the function. Once there are no more () tags
#  to process, then it returns the number instead of calling the function. At the end the cumulative number
#  is the answer. Simple, right? Not quite - this version still running. Will try removing the prints to see if that
#  speeds it up.
#  WHATT?!? After about an hour I got 11451628995...success!!!
#
# I'll work on a more efficient solution someday, but for now - on to Day 10!
