# Code written by @gerty

# Input from Day 10, Problem 1 (and 2) of Advent of Code 2016
# Input files in same directory
# My input: in file D10input.txt

class Bot:
    """Common robot with high/low destination tracking"""

    def __init__(self):
        self.chips = []          # nums is a list of the chips that a Bot has
        self.lowgive = 0        # the lesser of two chips will be given to this numbered bot next
        self.highgive = 0       # the greater of two chips will be given to this numbered bot next

    def assigntasks(self, low, high):
        self.lowgive = low
        self.highgive = high
        return

    def take(self, chip):
        self.chips.append(chip)      #  put the new arrival at the end of the list
        self.chips = self.chips.sort()            #  then sort the list so the high number is always at the end
        return

    def compare(self):
        if len(self.chips) > 1:
            return[self.chips.pop(), self.highgive,          #  Pop the high number and its destination
                   self.chips.pop(), self.lowgive]           #  then pop the low number and where it goes
            # we will be left with an empty list of nums now, if always at most 2 are in list
        else:
            return[]

    def isfull(self):
        if len(self.chips) == 2:
            print("TRUE", self.chips)
            return True
        else:
            return False

    def printme(self):
        print("For", self.chips, "low goes to", self.lowgive, "and high goes to", self.highgive)

answer = False
fleet = []
for i in range(600):
    fleet.append(Bot())

with open('Day10input.txt', 'r') as f:
    filedata = f.readlines()

for line in filedata:
    parsed = line.split()     # (e.g. "value 31 goes to bot 114" or "bot 182 gives low to bot 49 and high to bot 176")
    if parsed[0] == 'value':    # then parsed[5] is the bot, and parsed[1] is the chip
        fleet[int(parsed[5])].take(int(parsed[1]))   # bot takes the chip
        print("Bot", parsed[5], "took", parsed[1])
    if parsed[0] == 'bot':     # then parsed[1] is the bot, parsed[6] is low assignment, and parsed[11] is high
        destinationlow = int(parsed[6])
        destinationhigh = int(parsed[11])
        if parsed[5] == 'output':                           # Capturing outputs as a value greater than 500
            destinationlow += 300
        if parsed[10] == 'output':                          # Capturing outputs as a value greater than 500
            destinationhigh += 300
        fleet[int(parsed[1])].assigntasks(destinationlow, destinationhigh)  # Make assignment to the bot
        print("Bot", parsed[1], "will send low to", destinationlow, "and high to", destinationhigh)

while answer == False:
    for i in range(600):               # Keeping a range of 1000 spots - outputs are 500 and above
        if fleet[i].isfull():
            local = fleet[i].compare()  # local captures two chips if there is a chip that moves
            print('FULL: ', local)
            fleet[local[0]].take(local[1])  # This line gives the high number to its particular taker
            fleet[local[0]].printme()
            fleet[local[2]].take(local[3])  # This line gives the low number to its particular taker
            fleet[local[2]].printme()
            print(local[1], "to", local[0])
            print(local[3], "to", local[2])
            if (local[0] == 17) and (local[2] == 61):
                print('The winner is: Robot ', i)
                answer = True
for x in range(600):
    if fleet[x].isfull():
        fleet[x].printme()
