# Task 3.3
##Write a program which asks the user to enter a series of integers (one after another). The
##program should store the input values in a list. The program should keep asking for integers
##until a sentinel value (of your choice) is entered.
##Once the user has finished entering values, the program should output whole list of entered
##values sorted from smallest to largest, followed by the the number of even numbers and the
##number of odd numbers entered.


lst = []
input_number = int(input("Please enter an integer (enter a negative number to finish): "))
while input_number > 0 :
    lst.append(input_number)
    input_number = int(input("Please enter an integer (enter a negative number to finish): "))

lst.sort()
print(lst)

even_list = []
odd_list = []
for i in lst:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)


print(even_list)
print(odd_list)
    
