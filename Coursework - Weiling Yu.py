## This program allows user for playing Nim.
#  In the game of Nim, an arbitrary number of piles of tokens are formed, each with an arbitrary number of
#  tokens in them, and two players alternate in removing one or more tokens from any one pile. The player who
#  takes the last token is declared to be the winner.


from random import randint

# give the user the option of playing against the computer rather than a second human player.
option_against_computer = input("Do you want to play this game against with computer? (Y/N): ").upper()

# asking the user how many piles they would like to play with
pile_number = int(input("How many piles would like to play with? "))
print()

# And how many tokens they want in each pile and store the answer in the list 
tokens_list = []
for pile in range(pile_number) :
    tokens = int(input("Enter number of tokens in pile " + str(pile + 1) + ": "))
    tokens_list.append(tokens)

# print a representation of all token piles.    
for pile in range(pile_number):
    print("Token pile " + str(pile + 1) + ": " + "* " * tokens_list[pile])
print()

# start the game
if option_against_computer == "Y": # play against computer
    while max(tokens_list) > 0:
        # player's turn        
        done = False # boolean flag 
        while not done:
            player_pile_choice = int(input("Which pile do you want to remove tokens from: "))
            removed_player = int(input("And how many: ")) # number of tokens removed by player
            
            # validation process 
            if player_pile_choice > 0 and player_pile_choice  <= pile_number and removed_player > 0 and removed_player <= tokens_list[player_pile_choice - 1]:
                done = True
            else: 
                print("Invalid pile chocie or invalid removing tokens number, please try again. \n")

        tokens_list[player_pile_choice - 1] = tokens_list[player_pile_choice - 1] - removed_player # update the remaining tokens in the piles
 
        # Display the result 
        for pile in range(pile_number):
            print("Token pile " + str(pile + 1) + ": " + "* " * tokens_list[pile])
        print()

        # Display the winner message 
        if max(tokens_list) == 0:
            print("No more tokens in the piles, you win!") # if player didn't win, then computer's turn.
          
        
        # -----------------------------------------------------------------------------
        # computer's turn
        # Choose a random (nonempty) pile
        computer_pile_choice = randint(1,len(tokens_list))
        value = tokens_list[computer_pile_choice - 1]
        while value == 0:
            computer_pile_choice = randint(1,len(tokens_list))
            value = tokens_list[computer_pile_choice - 1]
            
            if max(tokens_list) == 0:
                break
            
        tokens_removed = randint(1, value)  
        tokens_list[computer_pile_choice - 1] = value -  tokens_removed
        
        # Display the result 
        print(tokens_removed, "tokens removed by computer from pile", computer_pile_choice)
        print()
       
        for pile in range(pile_number):
            print("Token pile " + str(pile + 1) + ": " + "* " * tokens_list[pile])
        print()

        # Display the winner message
        if max(tokens_list) == 0:
            print("No more tokens in the piles, computer wins!") # if player 1 didn't win, then computer's turn.
           
        
# --------------------------------------------------------------------------------------------------------------------

else: # play against human player
    while max(tokens_list) > 0:
        # player 1's turn
        print("Player 1's turn.")
        done = False # boolean flag 
        while not done:
            player1_pile_choice = int(input("Which pile do you want to remove tokens from: "))
            removed_player1 = int(input("And how many: ")) # number of tokens removed by player
            
            # validation process 
            if player1_pile_choice > 0 and player1_pile_choice  <= pile_number and removed_player1 > 0 and removed_player1 <= tokens_list[player1_pile_choice - 1]:
                done = True
            else: 
                print("Invalid pile chocie or invalid removing tokens number, please try again. \n")

        tokens_list[player1_pile_choice - 1] = tokens_list[player1_pile_choice - 1] - removed_player1 # update the remaining tokens in the piles

        # Display the result 
        for pile in range(pile_number):
            print("Token pile " + str(pile + 1) + ": " + "* " * tokens_list[pile])
        print()

        # Display the winner message 
        if max(tokens_list) == 0:
            print("No more tokens in the piles, player 1 wins!") # if player 1 didn't win, then player 2's turn.
            
        
        # -----------------------------------------------------------------------------
        # player 2's turn
        print("Player 2's turn.")
        done = False # boolean flag 
        while not done:
            player2_pile_choice = int(input("Which pile do you want to remove tokens from: "))
            removed_player2 = int(input("And how many: ")) 
            
            # validation process 
            if player2_pile_choice > 0 and player2_pile_choice  <= pile_number and removed_player2 > 0 and removed_player2 <= tokens_list[player2_pile_choice - 1]:
                done = True
            else: 
                print("Invalid pile chocie or invalid removing tokens number, please try again. \n")

        tokens_list[player2_pile_choice - 1] = tokens_list[player2_pile_choice - 1] - removed_player2 # update the remaining tokens in the piles
 
        # Display the result 
        for pile in range(pile_number):
            print("Token pile " + str(pile + 1) + ": " + "* " * tokens_list[pile])
        print()

        # Display the winner message 
        if max(tokens_list) == 0:
            print("No more tokens in the piles,, player 2 wins!") 
           
            
        

                              
