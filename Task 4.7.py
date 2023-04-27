# Task 4.7
# Create a function that has as a parameter a list of integers, representing the number of tokens
# in an arbitrary number of piles. The function should print a representation of the piles to the screen.
from random import randint

def main():
    tokens([5,7,8,6,4])
    computer([3,7,8,6,4])
    print(user([5,7,8,6,4]))

def tokens(lst):
    for i in lst:
        print("*" * i)


## Create a function that has as a parameter a list of integers, representing the token piles. The
## function should return the list with a random number of tokens removed from a randomly
## selected pile.
##
def computer(lst):
    value = 0 
    while value == 0:
        pile = randint(0,len(lst)-1)
        value = lst[pile]
        lst[pile] = value - randint(1,value)
        print(lst)


# Create a function that has as a parameter a list of integers, representing the token piles. The
# function should prompt the user to select a pile and a number of tokens to remove from that
# pile, then return the resulting list.

def user(lst):
     pile_remove_by_user = int(input("Which pile do you want to remove tokens from? "))
     number_remove_by_user = int(input("How many tokens would you like to remove? "))
     lst[pile_remove_by_user-1] = lst[pile_remove_by_user-1] - number_remove_by_user
     return lst
     
main()
