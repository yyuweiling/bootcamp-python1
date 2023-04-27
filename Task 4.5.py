# Task 4.5
# Write a function which takes an integer n as an argument and returns the n-th Fibonacci number.

def main():
    value = int(input("Please enter an integer: "))
    print(Fibonacci(value))

def Fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    nth_fibonacci = Fibonacci(n-1) + Fibonacci(n-2)
    return nth_fibonacci

main()
