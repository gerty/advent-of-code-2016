#!/usr/bin/python
# Code written by @gerty
# 12-19-2016

# Input from Day 11, Problem 1 of Advent of Code
# Input files in same directory
# My input from Day11input.txt:
# The first floor contains
#   a promethium generator and              (G0)
#   a promethium-compatible microchip.      (M0)
# The second floor contains
#   a cobalt generator,                     (G1)
#   a curium generator,                     (G2)
#   a ruthenium generator, and              (G3)
#   a plutonium generator.                  (G4)
# The third floor contains
#   a cobalt-compatible microchip,          (M1)
#   a curium-compatible microchip,          (M2)
#   a ruthenium-compatible microchip, and   (M3)
#   a plutonium-compatible microchip.       (M4)
# The fourth floor contains nothing relevant.

import random

# Tracking variables:
elevator = 1
generators = [1, 2, 2, 2, 2]
microchips = [1, 3, 3, 3, 3]
genmove = [0, 0, 0, 0, 0]
micmove = [0, 0, 0, 0, 0]
totalmoves = 0
success = False
bestmoves = 1000000

# Checking functions:
def legalstate(elev, gens, micros):
    if (elev not in gens) and (elevator not in micros):  # elev functions if contains at least one RTG / chip
        return False
    for x in range(5):
        if gens[x] != micros[x]:  # if generator is not with its microchip
            if micros[x] in gens:  # and if microchip floor contains any generators
                return False                # then invalid due to frying of microchip
    if (elevator not in micros) and (elevator not in gens):  # lonely elevator
        return False

# Not the efficient or elegant solution, but given the highly constraining rules, I decided to have parts randomly
# whether to get on a randomly moving elevator. I will cap the number of moves at the most successful solution, making
# the number get smaller and smaller as it goes. Well, we'll see...
while not success:
    genmove = [0, 0, 0, 0, 0]  # track movements of the generators
    micmove = [0, 0, 0, 0, 0]  # track movements of the microchips
    elevdir = int(0)
    if elevator == 1:  # must go up
        elevdir = 1
    if elevator == 4:  # must go down
        elevdir = -1
    if elevator == 2 or elevator == 3:
        elevdir = random.choice(-1,1)   # makes a random choice between up and down
    for i in range(5):
        if generators[i] == elevator:   # considering only generators that are on the same floor as an elevator
            genmove[i] = random.choice(0, elevdir)  # choose randomly whether to get on it or not
        if microchips[i] == elevator:   # considering only microchips that are on the same floor as an elevator
            micmove[i] = random.choice(0, elevdir)  # choose randomly whether to get on it or not
    passengers = genmove.count(elevdir) + micmove.count(elevdir)
    if 0 < passengers <= 2:  # if moving parts is between 1 and 2
        if legalstate(elev + elevdir, generators + genmove, microchips + micmove):  # legal future state test
            elev += elevdir
            generators += genmove
            microchips += micmove
            totalmoves += 1
    if generators == microchips == [4, 4, 4, 4, 4]:  # if all items are on 4th floor
        success = True
        print(totalmoves, "as a new minimum number of moves!")
        bestmoves = totalmoves
    if totalmoves >= bestmoves:  # if we have failed to beat our best score
        elevator = 1
        generators = [1, 2, 2, 2, 2]
        microchips = [1, 3, 3, 3, 3]
        totalmoves = 0
        print("Best is still:", bestmoves)

# Saving this version without testing for now. General idea might be sound, but more monte carlo than efficient.



