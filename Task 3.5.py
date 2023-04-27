##Write a program which reads numbers and adds them to a list if they are not already in the
##list. Once there are 5 numbers in the list, the program should print the contents of the list and
##terminate.


lst=[]
NUMBER = 5

while len(lst) < NUMBER:
    input_number = int(input("please input a number: "))
    if input_number not in lst:
        lst.append(input_number)
    
print(lst)

