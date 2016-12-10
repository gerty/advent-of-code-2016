# Code written by @gerty

# Input from Day 7, Problem 1 of Advent of Code 2016
# Input files in same directory
# My input: in file D7input.txt

answer = 0


def isThisABBA(clip):  # A function to look at 4 characters for the match
    if len(clip) != 4:  # Error-check for a wrongly sized string
        return False
    if clip[0] == clip[1]:  #first catch the case where all might be the same
        return False
    if clip[0] + clip[1] == clip[3] + clip [2]:  # then check for the true ABBA case
        return True
    else:
        return False

def searchLineForABBA(target):
    ch = 0
    inbrackets = False  # Keep track of whether we're starting the search from inside or outside brackets..
    hasABBA = False   # ...because finding an ABBA does not necessarily mean we return a True
    while ch < len(line)-4:  # (no point in starting further than 4 from end)
        if line[ch] == '[':  # removed the '\' from '\[' - that was a surprise
            inbrackets = True   # After finding '[' make inBrackets True until finding ']'
        if line[ch] == ']':
            inbrackets = False  # After finding ']' inBrackets goes back to False (no point in finding ']' near EOL)
        if isThisABBA(line[ch:ch+4]):
            print(line[ch:ch+4])
            if inbrackets:
                return False  # if ABBA is found in brackets, it is not allowed to be an ABBA
            else:
                hasABBA = True  # don't want to return True yet - there might be an ABBA in brackets still
        ch += 1
    return hasABBA  # only return True if found ABBA without early escape from def

with open('D7input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    if searchLineForABBA(line):
        answer += 1

print(answer)


# Saving initial thoughts until solution is done to see how close I got...
# Loop through lines of input file.
    # go into looking mode fr each line until you hit a "["
        # looking mode looks for ABBA patterns but rejects AAAA patterns
        # selecting any two letters, check the two ahead of it, unless you reach a '[' or a '\n'
        # but clearly those two cases would fail the match anyway, so really just check the two ahead
        # maybe have to be careful of the EOF case
        # when we hit '[', traverse until we see ']' and then continue until EOL
    # capture everything inside the [] for later (probably part 2), and the 4-char ABBA
# but just count them for now and return that as the answer

#  Also, I feel like I commented this one well enough that it should just work the first time without errors.
#  Well, there were only a few syntax errors, but first attempt at an answer of 190 was too high.
#  Learned that you don't need escape characters before brackets in a string(char) definition.
#  Second attempt (115) was correct!
