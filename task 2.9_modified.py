from random import randint

token_input = input("How many tokens would you like in the piles? ")
tokens = token_input.split(",")
tokens_pile1 = int(tokens[0])
tokens_pile2 = int(tokens[-1])
tokens_rep = "*"


print("pile 1: " + tokens_rep * tokens_pile1)
print("pile 2: " + tokens_rep * tokens_pile2 + "\n")

number_remove_by_user = 0


# users' turn:
valid = False
while not valid:
    pile_remove_by_user = int(input("Which pile do you want to remove tokens from? "))
    if pile_remove_by_user == 1: # remove tokens from pile 1 by user
        number_remove_by_user = int(input("How many tokens would you like to remove? "))
        tokens_pile1 = tokens_pile1 - number_remove_by_user
        valid = True

    elif pile_remove_by_user == 2: # remove tokens from pile 2 by user
        number_remove_by_user = int(input("How many tokens would you like to remove? "))
        tokens_pile2 = tokens_pile2 - number_remove_by_user
        valid = True

    else :
        print("Please select valid pile.")

print("pile 1: " + tokens_rep * tokens_pile1)
print("pile 2: " + tokens_rep * tokens_pile2 + "\n")

#--------------
## Computer's turn:
#---------------------
# Choose a random (nonempty) pile
if tokens_pile1 == 0 :
    computerPileChoice = 2
elif tokens_pile2 == 0 :
    computerPileChoice = 1
else : 
    computerPileChoice = randint(1, 2)

# Choose a random number of tokens to remove from the pile
if computerPileChoice == 1 :
    tokensRemoved = randint(1,tokens_pile1)
    tokens_pile1 = tokens_pile1 - tokensRemoved
else :
    tokensRemoved = randint(1, tokens_pile2)
    tokens_pile2 = tokens_pile2 - tokensRemoved

# Display the result
print(tokensRemoved, "tokens removed from pile", computerPileChoice)
print()
print("Token piles:")
print("pile 1: ", "*" * tokens_pile1)
print("pile 2: ", "*" * tokens_pile2)
print()
#---------------------

