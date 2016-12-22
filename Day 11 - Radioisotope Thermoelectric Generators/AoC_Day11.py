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

# Tracking variables:
elevator = 1
generators = [1, 2, 2, 2, 2]  # locations of each generator
microchips = [1, 3, 3, 3, 3]  # locations of each microchip
beenthere = [elevator, generators, microchips]       # keep track of states we have covered without repeating
genmove = [0, 0, 0, 0, 0]     # movement of each generator
micmove = [0, 0, 0, 0, 0]     # movement of each microchip

# This next approach will keep track of all of the states that we have already covered. If it reaches a duplicate,
# it will show it as an invalid move - essentially a wall in a multi-dimensional maze.

# The coded representation of a state will be a list of 3 items: 1 integer and 2 lists of 5 integers each
# This list will be [elevator floor, [5 floors which G0-G4 are located], [5 floors which M0-M4 are located]]
# The Generators and Microchips are encoded with G0-G4 and M0-M4 per above in the comments.

# We will have a few helper functions checking states for legality, and one iterative solver function, which will
# calculate the minimum distance to a solution, much in the way the maze problem was (should have been) solved.

# There is some very helpful info here: https://docs.python.org/2/tutorial/datastructures.html


# Checking function for a legal state:
def legalstate(elev, gens, micros):   # Sending list of [elev, [gens], [micros]]
    if [elev, gens, micros] in beenthere:
        return False                # covering the "been there" case
    for x in range(5):
        if gens[x] != micros[x]:    # if generator is not with its microchip
            if micros[x] in gens:   # and if microchip floor contains any generators
                return False        # then we have the "invalid due to frying of microchip" case
    if (elev < 1) or (elev > 4):
        return False                # checking for the invalid floor case
    return True


def legalmove(elev1, gens1, mics1, elev2, gens2, mics2):  # Check if a move from state 1 to state 2 is valid
    if not legalstate(elev2, gens2, mics2):  # Check right away for the valid end state
        return False           # Get out quickly if state 2 is invalid
    elevmove = elev2 - elev1  # Capture a positive or negative move of 1 or -1
    gensmove = []
    micsmove = []
    for x in range(len(gens1)):
        gensmove.append(gens2[x]-gens1[x])
        micsmove.append(mics2[x]-mics1[x])
    if gensmove.count(elevmove) + micsmove.count(elevmove) == 0:  # ensuring something has same move as the elevator
        return False
    if gensmove.count(elevmove) + micsmove.count(elevmove) > 2:  # ensuring no more than two move with the elevator
        return False
    if gensmove.count(-elevmove) + micsmove.count(-elevmove) > 0:  # ensuring no other moves unless on this elevator
        return False
    return True


def reach(elev, gen, micro):  # Finds the eligible paths forward, returning number of moves to an answer, or None
    beenthere.append([elev, gen, micro])  # Record that we have checked this state for possible shortest path
    minimumpath = None    # Keep track of the min number of steps deep in this branch, so we return the lowest
    for direction in [-1, 1]:    # For either direction, all go together. Now we need to pick two passengers.
        g2 = gen  # Mirror list of generators from params
        m2 = micro  # Mirror list of microchips from params
        for gm in range(10):      # For any eligible generators (0-4) and microchips (5-9)
            if gm < 5:
                g2[gm] += direction     # Make sure the one chosen rides in the right direction (-1 or +1)
            if gm > 4:
                m2[gm-5] += direction   # Make sure the one chosen rides in the right direction (-1 or +1)
            for gm2 in range(10):  # For any eligible generators (0-4) and microchips (5-9)
                if gm2 < 5:
                    if gm2 != gm:       # Just in case we choose the same item, don't send it up two floors
                        g2[gm2] += direction  # Make sure the one chosen rides in the right direction (-1 or +1)
                if gm2 > 4:
                    if gm2 != gm:       # Just in case we choose the same item, don't send it up two floors
                        m2[gm2 - 5] += direction  # # Make sure the one chosen rides in the right direction (-1 or +1)
            if legalmove(elev, gen, micro, elev + direction, g2, m2):  # Let's go! See if that move would be legal.
                path = reach(elev + direction, g2, m2)  # check path for valid solution
                if path and minimumpath:    # path returns None if no path is found - need to check for this case
                    if minimumpath > path:      # if path (solution) is produced that is less than minimum found so far
                        minimumpath = path      # make this number the shortest path to victory
                if path and not minimumpath:
                    minimumpath = path          # if no minimum path has been found on this branch yet
    return minimumpath


print(reach(elevator, generators, microchips))


# Original failed method below for archiving purposes
""""
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
"""
