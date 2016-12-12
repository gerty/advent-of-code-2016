# Code written by @gerty

# Input from Day 8, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D8input.txt

import numpy as np
import matplotlib.pyplot as plt

answer = 0
screen = np.zeros((6, 50))
makex = 0
makey = 0

def revealScreen(myscreen):  # print data on screen
    plt.imshow(myscreen, cmap=plt.cm.binary)
    #plt.scatter(myscreen, myscreen, )
    plt.show()


with open('D8input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    words = line.split()
    print(words)
    if words[0] == 'rect':
        makex = int(words[1].split('x')[0])
        makey = int(words[1].split('x')[1])
        for i in range(makex):
            for j in range(makey):
                screen[j][i] = 1   # still not sure why I had to switch these
    if words[0] == 'rotate':
        if words[1] == 'column':
            col = int(words[2].split('=')[1])  # captures even the most stubborn of multi-char column values
            num = int(words[4])                # captures length of column shift
            print(col, num)
            screen = screen.transpose()   # Need to transpose before and after in order to shift up and down
            screen[col] = np.roll(screen[col],num)
            screen = screen.transpose()
        if words[1] == 'row':
            row = int(words[2].split('=')[1])  # captures even the most stubborn of multi-char row values
            num = int(words[4])                # captures length of row shift
            print(row, num)
            screen[row] = np.roll(screen[row],num)

revealScreen(screen)   # <-- That was a fun reveal! "RURUCEOEIL"
answer = np.sum(screen)
print(answer)

# First answer that comes through is 121. Woo-hoo! That was it!
# And since I was experimenting with the plot-ability of it, a simple uncomment brought me to the RURUCEOEIL part 2.
