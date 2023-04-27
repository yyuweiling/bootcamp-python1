# Task 3.8
TICKET_PRICE= [[8.00, 8.00, 8.00, 8.00, 8.00, 8.00],
                [8.00, 8.00, 8.00, 8.00, 8.00, 8.00],
                [8.00, 9.99, 9.99, 9.99, 9.99, 8.00],
                [8.00, 9.99, 9.99, 9.99, 9.99, 8.00],
                [9.99, 9.99, 9.99, 9.99, 9.99, 9.99],
                [9.99, 12.50, 12.50, 12.50, 12.50, 9.99],
                [9.99, 12.50, 12.50, 12.50, 12.50, 9.99],
                [8.00, 9.99, 12.50, 12.50, 9.99, 8.00],
                [8.00, 9.99, 9.99, 9.99, 9.99, 8.00],
                [8.00, 8.00, 8.00, 8.00, 8.00, 8.00]]

ROWLETTER = "ABCDEFGHIJ"

user_input = input("Please choose your seat in the format letter/number (enter a number greater than 6 to finish): ")
total_cost = 0

row = user_input.split("/")[0]  #accessing the row element of user input
column = user_input.split("/")[1] # accessing the column element of user input

while int(column) <= 6: # as long as the column number entered by user is less than 7, enter the loop
    seat_cost = TICKET_PRICE[int(ROWLETTER.index(row))][int(column)-1] # acess the ticket price for each selected seat.
    total_cost = total_cost + float(seat_cost) # updating the total cost
    print("This seat costs: " + str(seat_cost))
    user_input = input("Please choose your seat in the format letter/number (enter a number greater than 6 to finish): ")# ask for another input
    row = user_input.split("/")[0]
    column = user_input.split("/")[1]


print("The total cost is %.2f" % total_cost)
    
