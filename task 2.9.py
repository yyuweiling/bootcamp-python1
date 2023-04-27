from random import randint

token_input = input("How many tokens would you like in the piles? ")
tokens = token_input.split(",")
tokens_pile1 = int(tokens[0])
tokens_pile2 = int(tokens[-1])
tokens_rep = "*"


print("pile 1: " + tokens_rep * tokens_pile1)
print("pile 2: " + tokens_rep * tokens_pile2 + "\n")


pile_remove_by_user = int(input("Which pile do you want to remove tokens from? "))
number_remove_by_user = 0


if pile_remove_by_user == 1: # remove tokens from pile 1 by user
    number_remove_by_user = int(input("How many tokens would you like to remove? "))
    tokens_pile1 = tokens_pile1 - number_remove_by_user
    print("pile 1: " + tokens_rep * tokens_pile1)
    print("pile 2: " + tokens_rep * tokens_pile2 + "\n")
    if tokens_pile1 >=1:
        random_pile_remove_by_computer = randint(1,2)
        if random_pile_remove_by_computer == 1: # if computer randomly chosen pile 1
            random_tokens_remove_by_computer = randint(1,tokens_pile1)  # computer select a random number of tokens    
            print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile " + str(random_pile_remove_by_computer) + "!")
            tokens_pile1 = tokens_pile1 - random_tokens_remove_by_computer
            print("pile 1: " + tokens_rep * tokens_pile1)
            print("pile 2: " + tokens_rep * tokens_pile2)
        else : # if computer randomly chosen pile 2
            random_tokens_remove_by_computer = randint(1,tokens_pile2)  # computer select a random number of tokens    
            print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile " + str(random_pile_remove_by_computer) + "!")
            tokens_pile2 = tokens_pile2 - random_tokens_remove_by_computer
            print("pile 1: " + tokens_rep * tokens_pile1)
            print("pile 2: " + tokens_rep * tokens_pile2)
    else :# computer forced to chose pile 2
        random_tokens_remove_by_computer = randint(1,tokens_pile2)
        print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile 2!")
        tokens_pile2 = tokens_pile2 - random_tokens_remove_by_computer
        print("pile 1: " + tokens_rep * tokens_pile1)
        print("pile 2: " + tokens_rep * tokens_pile2)
         
      

elif pile_remove_by_user == 2: # remove tokens from pile 2 by user
    number_remove_by_user = int(input("How many tokens would you like to remove? "))
    tokens_pile2 = tokens_pile2 - number_remove_by_user
    print("pile 1: " + tokens_rep * tokens_pile1)
    print("pile 2: " + tokens_rep * tokens_pile2 + "\n")
    if tokens_pile2 >=1:
        random_pile_remove_by_computer = randint(1,2)
        if random_pile_remove_by_computer == 1: # if computer randomly chosen pile 1
            random_tokens_remove_by_computer = randint(1,tokens_pile1)  # computer select a random number of tokens    
            print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile " + str(random_pile_remove_by_computer) + "!")
            tokens_pile1 = tokens_pile1 - random_tokens_remove_by_computer
            print("pile 1: " + tokens_rep * tokens_pile1)
            print("pile 2: " + tokens_rep * tokens_pile2)
        else : # if computer randomly chosen pile 2
            random_tokens_remove_by_computer = randint(1,tokens_pile2)  # computer select a random number of tokens    
            print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile " + str(random_pile_remove_by_computer) + "!")
            tokens_pile2 = tokens_pile2 - random_tokens_remove_by_computer
            print("pile 1: " + tokens_rep * tokens_pile1)
            print("pile 2: " + tokens_rep * tokens_pile2)
    else :# computer forced to chose pile 1
        random_tokens_remove_by_computer = randint(1,tokens_pile1)
        print("I remove " + str(random_tokens_remove_by_computer) + " tokens from pile 1!")
        tokens_pile1 = tokens_pile1 - random_tokens_remove_by_computer
        print("pile 1: " + tokens_rep * tokens_pile1)
        print("pile 2: " + tokens_rep * tokens_pile2)
else :
    print("Please select valid pile.")



                      

