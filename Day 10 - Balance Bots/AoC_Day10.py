# Code written by @gerty

# Input from Day 10, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D10input.txt

class Bot:
    """Common robot with high/low destination tracking"""

    def __init__(self):
        self.chiplow = 0        # these slots hold the number of the chip, 0 if empty
        self.chiphigh = 0
        self.lowgive = 0        # the lesser of two chips will be given to this numbered bot next
        self.highgive = 0       # the greater of two chips will be given to this numbered bot next

    def assigntasks(self, low, high):
        self.lowgive = int(low)
        self.highgive = int(high)
        return

    def give(self, chipnum):   # horribly inefficient way to track chips, but tuples and sort() weren't working :/
        if self.chiplow == 0 and self.chiphigh > 0:   # One chip only
            self.chiplow = chipnum
        if self.chiphigh == 0:  # Empty bot if high chip is zero
            self.chiphigh = chipnum
        if self.chiplow > self.chiphigh:  # after assigning, check for low and high in order
            tempchip = self.chiphigh
            self.chiphigh = self.chiplow
            self.chiplow = tempchip
        return True

    def compare(self):
        if self.chiplow > 0 and self.chiphigh > 0:   # full of chips
            temphigh = self.chiphigh
            templow = self.chiplow

            self.chiphigh = 0
            self.chiplow = 0

            return [temphigh, self.highgive,
                    templow, self.lowgive]
        else:
            return[]

    def isfull(self):
        if (self.chiplow != 0) and (self.chiphigh != 0):  # full of chips
            return True
        else:
            return False

    def printme(self):
        print(self.chiplow, "goes to", self.lowgive, "and", self.chiphigh, "goes to", self.highgive)

answer = False
fleet = []
for i in range(600):
    fleet.append(Bot())

with open('Day10input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    parsed = line.split()     # (e.g. "value 31 goes to bot 114" or "bot 182 gives low to bot 49 and high to bot 176")

    if parsed[0] == 'value':    # parsed[5] is the bot, and parsed[1] is the chip
        fleet[int(parsed[5])].give(int(parsed[1]))   # bot takes the chip

    if parsed[0] == 'bot':     # parsed[1] is the bot, parsed[6] is low assignment, and parsed[11] is high
        destinationlow = int(parsed[6])
        destinationhigh = int(parsed[11])
        if parsed[5] == 'output':
            destinationlow += 300        # Capturing outputs as a value greater than 300
        if parsed[10] == 'output':
            destinationhigh += 300       # Capturing outputs as a value greater than 300
        fleet[int(parsed[1])].assigntasks(destinationlow, destinationhigh)  # Make assignment to the bot

while answer == False:
    for i in range(600):               # Keeping a range of 600 spots - outputs are 300 and above
        if fleet[i].isfull():
            local = fleet[i].compare()  # local looks at these two chips
            print(i, "is FULL:", local)
            fleet[local[1]].give(local[0])  # This line gives the high number to its particular taker
            fleet[local[3]].give(local[2])  # This line gives the low number to its particular taker
            print("Value", local[0], "to", local[1])
            print('Value', local[2], "to", local[3])
            if (int(local[0]) == 61) and (int(local[2]) == 17):
                print('The winner is: Robot ', i)
                answer = True
for x in range(600):
    if fleet[x].isfull():
        print(x)
        fleet[x].printme()

# After much coding and re-coding, I found that my search criteria was swapping high and low
# First try was a success. Robot 47 was the winner.
