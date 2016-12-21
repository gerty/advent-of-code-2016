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
generators = [1, 2, 2, 2, 2]  # locations of each generator
microchips = [1, 3, 3, 3, 3]  # locations of each microchip
genmove = [0, 0, 0, 0, 0]     # movement of each generator
micmove = [0, 0, 0, 0, 0]     # movement of each microchip
totalmoves = 0              # tracks total moves in each try
success = False             # looks for success criteria
bestmoves = 1000000         # artificially high starting point
beenthere = [elevator, generators, microchips]       # keep track of states we have covered without repeating


# Checking functions:
def legalstate(elev, gens, micros):
    if [elev, gens, micros] in beenthere:  # covering the "been there" case
        return False
    for x in range(5):
        if gens[x] != micros[x]:  # if generator is not with its microchip
            if micros[x] in gens:  # and if microchip floor contains any generators
                return False                # then cover the invalid due to frying of microchip case
    if (elev1 < 1) or (elev1 > 4):
        return False
    if (elev2 < 1) or (elev2 > 4):
        return False                # covering the invalid floor case
    return True

def legalmove(elev1, gens1, mics1, elev2, gens2, mics2):
    elevmove = elev2 - elev1
    gensmove = []
    micsmove = []
    for x in range(5):
        gensmove.append(gens2[x]-gens1[x])
        micsmove.append(mics2[x]-mics1[x])
    if gensmove.count(elevmove) + micsmove.count(elevmove) == 0:  # covering the at least one case
        return False
    if gensmove.count(elevmove) + micsmove.count(elevmove) > 2:  # covering the no more than two-at-a-time case
        return False
    if gensmove.count(-elevmove) + micsmove.count(-elevmove) > 0:  # covering the all inthe same direction case
        return False
    return True

#def getdistance(elev, gen, micro):  # Finds the eligible paths forward and iterates
#    possible = []
#    for dir in [-1,1]:      # For both directions
#        for g in range(5):      # For any eligible generators as the first passengers
#            for m in range(5):  # For any eligible microchips as the first passengers
#                possible.append([elev+dir, range[0:g] join??]
#                if .....        # Check for eligibility


while not success:
    genmove = [0, 0, 0, 0, 0]  # track movements of the generators
    micmove = [0, 0, 0, 0, 0]  # track movements of the microchips
    if elevator == 1:  # must go up
        elevdir = 1
    if elevator == 4:  # must go down
        elevdir = -1
    if elevator == 2 or elevator == 3:
        elevdir = random.choice([-1, 1])   # makes a random choice between up and down

    for i in range(5):
        if generators[i] == elevator:   # considering only generators that are on the same floor as an elevator
            genmove[i] = random.choice([0, elevdir])  # choose randomly whether to get on it or not
        if microchips[i] == elevator:   # considering only microchips that are on the same floor as an elevator
            micmove[i] = random.choice([0, elevdir])  # choose randomly whether to get on it or not

    if 1 <= genmove.count(elevdir) + micmove.count(elevdir) <= 2:  # if moving parts is between 1 and 2
        if legalstate(elevator + elevdir,
                      [x + y for x, y in zip(generators, genmove)],
                      [xx + yy for xx, yy in zip(microchips, micmove)]):  # legal future state test
            elevator += elevdir
            generators = [x + y for x, y in zip(generators, genmove)]
            microchips = [xx + yy for xx, yy in zip(microchips, micmove)]
            totalmoves += 1
            beenthere.append([elevator, generators, microchips])

    if generators == microchips == [4, 4, 4, 4, 4]:  # if all items are on 4th floor
        print(totalmoves, "as a new minimum number of moves!")
        bestmoves = totalmoves

    if totalmoves >= bestmoves:  # if we have failed to beat our best score
        elevator = 1
        generators = [1, 2, 2, 2, 2]
        microchips = [1, 3, 3, 3, 3]
        beenthere = [elevator, generators, microchips]
        totalmoves = 0
        print("Best is still:", bestmoves)

# Saving this version without testing for now. General idea might be sound, but more monte carlo than efficient.
# And now after testing I realize that it is not sound at all. Expecting a correct string of guesses to come up
# randomly is silly. Down to 691 after 5 minutes. Now 371. Need to make this iterative. Even eliminating repeat
# states doesn't work, since I can't detect a stuck case.

# Pushing this version and starting from scratch.

