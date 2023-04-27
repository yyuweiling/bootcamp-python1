# Task 4.6
# Create a recursive function that has as parameters a float x and an integer n. The function should return x**n.

def main():
    base = float(input("Please enter a value for the base: "))
    power = int(input("Please enter a value for the power: "))
    print(recursive(base, power))

def recursive(x, n):
    if n == 0:
        return 1
    if n >= 1:
        return x * recursive(x, n-1)
    if n < 0:
        return 1 / recursive(x,-n)

main()
