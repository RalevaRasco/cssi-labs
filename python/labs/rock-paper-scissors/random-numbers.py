import random

print("Welcome to Sam's Random Playground")

die1 = (random.randint(1,6))
die2 = (random.randint(1,6))

sum = die1 + die2

if die1 == die2:
    print("You move %s spaces. Roll again" % (sum))

else:
    print("You move %s spaces. Next player's turn." % (sum))
