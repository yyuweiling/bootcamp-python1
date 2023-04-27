#Task 1.5
from math import sqrt

#Users to input the length of sides a and b.
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

#calculate the hypotenuse.
h = sqrt(a**2 + b**2)

#print the output.

print("The length of the hypotenuse is:%.2f" % h)
