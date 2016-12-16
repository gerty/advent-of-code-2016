# Code written by @gerty

# Input from Day 10, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D10input.txt

class Bot:
    """Common robot with high/low destination tracking"""

    def __init__(self):
        self.nums = []             #  nums is a list of integers
        self.lowgive = 0         #  a low compare goes to this bot next
        self.highgive = 0       #  a high compare goes to this bot next
        # so far we make a big assumption here that each time through, that at most 2 chips can end up here in one move

    def assign(self, low, high):
        self.lowgive = low
        self.highgive = high
        return

    def take(self, chip):
        print(chip, self.nums)
        self.nums.append(chip)      #  put the new arrival at the end of the list
        self.nums.sort()            #  then sort the list so the high number is always at the end
        return

    def compare(self):
        if len(self.nums) > 1:
            return[self.nums.pop(), self.highgive,          #  Pop the high number and its destination
                   self.nums.pop(), self.lowgive]           #  then pop the low number and where it goes
            # we will be left with an empty list of nums now, if always at most 2 are in list
        else:
            return[]


answer = False
fleet = []
for i in range(1000):
    fleet.append(Bot())

with open('Day10input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    parsed = line.split()
    if parsed[0] == 'value':    # then parsed[5] is the bot, and parsed[1] is the chip
        fleet[int(parsed[5])].take(int(parsed[1]))   # assign the chip to the bot
    if parsed[0] == 'bot':     # then parsed[1] is the bot, parsed[6] is low assignment, and parsed[11] is high
        fleet[int(parsed[1])].assign(int(parsed[6]),
                                     int(parsed[11]))

while answer == False:
    for i in range(1000):
        local = fleet[i].compare()
        print(local)
        if local != []:
            fleet[local[0]].take(local[1])  # This line assigns the high number to its particular taker
            fleet[local[2]].take(local[3])  # This line assigns the low number to its particular taker
            if (local[0] == 17) and (local[2] == 61):
                print('The winner is: Robot ', i)
            answer = True

# TODO: Process the outputs