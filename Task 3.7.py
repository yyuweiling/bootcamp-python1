# Task 3.7
##Write a program that asks the user to enter some positive integer n.
##The program should print the pattern:
##    1
##   212
##  32123
## 4321234
##543212345
##where the height of the pattern should be n. That is, the above pattern is printed when nis 5.
##The above pattern would be one row higher if nwas 6.

user_input = int(input("Please enter a positive integer: "))

for i in range(1, user_input + 1):
    print(" "* (user_input -i), end="") # for each row, print spaces before printing the numbers
    for j in range ( i, 1, -1): #create the decreasing sequence, start with  nothing, then  2 in second row, 3,2 in third row
        print(j, end="")
    for k in range (1, i+1): # create the increasing sequence, starting with 1, then 1,2 in second row,1,2,3 in third row and so on.
        print(k, end="")
    print("")


