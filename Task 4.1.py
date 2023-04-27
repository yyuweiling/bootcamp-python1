# Task 4.1
# Write a function which has as a parameter the radius of a circle. The function should compute
# and return the area of a circle with that radius. 

def main():  #define main fnnction to test
    print(circle_area(4))
    print(circle_area(5))
    print(circle_area(8))
    
def circle_area(r):
    from math import pi  # import pi
    area = pi * (r ** 2) # compute the area of circle
    return area          # return the area

main()

