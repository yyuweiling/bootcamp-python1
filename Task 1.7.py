#Task 1.7

from random import randint
                    
#Users to input an integer to represent the number of tokens in a pile
tokens = int(input("How many tokens would you like in the pile? "))

#define the representation
tokenRep = "*"
iniTokenPile = tokenRep * tokens
#randomly select an integer
randInteger = randint(0,tokens)
#calculate the remainding number of tokens.
tokenRemain = tokens - randInteger
remTokenPile = tokenRep * tokenRemain

#print the initial token pile.
print("Token pile:",iniTokenPile)
#print the message saying number of tokens that was randomly removed by the copmputer.
print("I remove",randInteger,"tokens from the pile!")
#print the remaining token pile.
print("Token pile:",remTokenPile)



