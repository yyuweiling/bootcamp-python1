##Write a program which simulates tossing a coin 10 times. You can do this by having a for loop which:
##1. Generates either a 0 or a 1 randomly.
##2. If the number is 0, then print “Heads”, if the number is 1 then print “Tails”.

from random import randint

TOSSES = 10
 
for i in range(TOSSES): # for each toss
    random_number = randint(0,1) # generate a random number 0 or 1
    if random_number == 0: #If the number is 0, then print “Heads”
        print("Heads")
    else:
        print("Tails") # if the number is 1 then print “Tails”.
