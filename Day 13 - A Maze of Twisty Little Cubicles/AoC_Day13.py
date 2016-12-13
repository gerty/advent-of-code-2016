# Code written by @gerty

# Input from Day 13, Problem 1 of Advent of Code 2016
# Input files in same directory
# My input: 1350

import numpy as np
import matplotlib.pyplot as plt

myinput = 1350
screen = np.zeros((40, 40))
# 0=open, 1=wall
targetx = 31
targety = 39

x = 40
y = 40
temp = 0
tempstr = ''


def revealScreen(myscreen):  # plot walls and spaces
    plt.imshow(myscreen, interpolation='nearest')
    # , cmap=plt.cm.binary)
    plt.show()
    print(myscreen)


for j in range(y):
    for i in range(x):
        temp = i*i + 3*i + 2*i*j + j + j*j + 1350
        print(temp)
        tempstr = str(bin(temp))[2:]
        print(tempstr)
        if tempstr.count('1') % 2 == 0:
            screen[i][j] = 0
            print('even')
        else:
            screen[i][j] = 1
            print('odd')

revealScreen(screen)

# First guess, 73, done more or less by hand with a generated map. Problem exists that there is a wall in the way of
# the answer, (31,39). Assuming the user is able to step through that last wall, I'll try 74 next.
# 74 is also too low. Commit, push, sleep.
