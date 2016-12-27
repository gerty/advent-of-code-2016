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

import collections

# Tracking variables:
elevator = 1
generators = [1, 2, 2, 2, 2]  # locations of each generator
microchips = [1, 3, 3, 3, 3]  # locations of each microchip
beenthere = []       # keep track of states we have covered without repeating
beentheresets = ()

# This  approach will keep track of all of the states that we have already covered. If it reaches a duplicate,
# it will show it as an invalid move - essentially a wall in a multi-dimensional maze.

# The coded representation of a state will be a list of 3 items: 1 integer and 2 lists of 5 integers each
# This list will be [elevator floor, [5 floors which G0-G4 are located], [5 floors which M0-M4 are located]]
# The Generators and Microchips are encoded with G0-G4 and M0-M4 per above in the comments.

# We will have a helper function checking states for legality, and a recursive solver function, which will
# calculate the minimum distance to a solution, much in the way the maze problem was (should have been) solved.

# There is some very helpful info here: https://docs.python.org/2/tutorial/datastructures.html


def isEquivalentState(list1, list2):  # each list is a list of two lists
    pairs1 = collections.Counter()
    pairs2 = collections.Counter()
    for i in range(len(list1[0])):
        print(list1[0][i], list1[1][i])
        pairs1[[list1[0][i], list1[1][i]]] += 1  # Create pairs for gens (list1[0]) and micros (list1[1])
    for i in range(len(list2[0])):
        pairs2[[list2[0][i], list2[1][i]]] += 1  # Create pairs for gens (list2[0]) and micros (list2[1])
    if pairs1 == pairs2:
        return True

# This function checks for a legal state:
def legalstate(elev, gens, micros):   # Sending list of [elev, [gens], [micros]]
    if [elev, gens, micros] in beenthere:
        return False                # covering the "been there" case
    for state in beenthere:    # Cut search times by 120x? Look for the "been to equivalent state" condition
        if elev == state[0]:
            print(state[1:3], [gens, micros])
            if isEquivalentState(state[1:3], [gens, micros]):
                return False
    for x in range(5):
        if gens[x] != micros[x]:    # if generator is not with its microchip
            if micros[x] in gens:   # and if microchip floor contains any generators
                return False        # then we have the "invalid due to frying of microchip" case
    return True


# This function finds the eligible paths forward, returning number of moves to an answer, or None
def reach(elev, gen, micro, deep):
    if [elev, gen, micro] == [4, [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]:
        print("Deep:", deep, gen, micro)
        enterkey = input("Enter to continue:")
        return int(0)
    minimumpath = None    # Keep track of the minimum number of steps deep in this branch, so we return the lowest
    for upordown in [-1, 1]:    # For either direction, all go together. Now we need to pick two passengers.
        if (elev + upordown) in [1, 2, 3, 4]:  # is our elevator still on a valid floor?
            for riding in range(10):      # Generators (0-4) and microchips (5-9) could ride elevator
                g2 = gen[:]  # g2 is a "delta" state of a moved generator set (COPY it with [:] !!!!)
                m2 = micro[:]  # m2 is a "delta" state of a moved microchip set (COPY it with [:] !!!!)

                if riding < 5 and gen[riding] == elev:    # if riding is a generator on same floor as elevator
                    g2[riding] += upordown     # Assign the "delta" generator floor (-1 or +1)

                if riding > 4 and micro[riding - 5] == elev:  # if riding is a microchip on same floor as elevator
                    m2[riding - 5] += upordown   # Assign the "delta" microchip floor (-1 or +1)

                for ridingtoo in range(10):  # Possible second passenger, for eligible generators and microchips
                    g3 = g2[:]  # g3 is the second "delta" state - must reset after each search for 2nd passenger!
                    m3 = m2[:]  # m3 is the second "delta" state - must reset after each search for 2nd passenger!

                    if ridingtoo < 5 and gen[ridingtoo] == elev:  # ridingtoo on the same floor as elevator?
                        if ridingtoo != riding:    # Just in case we choose same item, don't send it up two floors
                            g3[ridingtoo] += upordown  # Assign the "delta" generator floor (-1 or +1)
                    if ridingtoo > 4 and micro[ridingtoo - 5] == elev:  # on the same floor as the elevator?
                        if ridingtoo != riding:  # Just in case we choose same item, don't send it up two floors
                            m3[ridingtoo - 5] += upordown  # Assign the "delta" microchip floor (-1 or +1)

                    if legalstate(elev + upordown, g3[:], m3[:]):  # removed: (g2 != gen or m2 != micro) and
                        beenthere.append([elev + upordown, g3[:], m3[:]])
                        path = reach(elev + upordown, g3[:], m3[:], deep + 1)  # Check path for a valid solution.
                        print("PATH=", path, minimumpath, gen, micro, "---", g3, m3, deep, "deep")
                        if (path is not None):
                            if (minimumpath is not None):  # if finding an additional solution
                                if path < minimumpath:  # only replace if it's a better solution
                                    minimumpath = path  # and make minimumpath equal the path just found
                            if (minimumpath is None):    # if this is the first solution
                                    minimumpath = path      # no minimum path has been found on this branch yet

    if minimumpath:
        print("*************************", minimumpath)
        enterkey = input("Found minpath")
        return minimumpath
    return None

print(reach(elevator, generators[:], microchips[:], 0))

# Using a cap of 50 returned 102 as an answer
# Answer 102 too high.
# interestingly half of that was how deep we went for an answer: 51, also too high
# Answer bring returned is consistently twice that of the capped number.
# But, after "fixing the code", and setting the cap at 50, it ran for about 90 minutes and returned None.
# Adding a watch for how deep the recursion goes showed it hanging at around 50 almost the whole time.

# Found an answer at 39 deep when using the sum of the lists as an indicator of how close the solution was.
# 39 is wrong. No indication anymore about high or low. 38 is wrong too. Suspicious that these wrong answers are so
# close to what I choose to cap the recursion at.
