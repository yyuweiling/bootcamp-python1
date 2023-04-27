#Task 3.9

##Write list comprehensions to generate:

##1. lst1, the list of integers between -10 and 10 (inclusive).

lst1 = [i for i in range(-10,11)]
print(lst1)
print(" ")

##2. lst2, the list of odd numbers in lst1.

lst2 = [i for i in lst1 if i % 2 == 1]
print(lst2)
print(" ")

##3. lst3, the list of squares of negative numbers in lst2.
lst3 = [i**2 for i in lst2 if i < 0]
print(lst3)
print(" ")

##4. lst4, the list of numbers in lst3 that contain a ‘9’ as a digit.

lst4 =[i for i in lst3 if "9" in str(i)]
print(lst4)
print(" ")
