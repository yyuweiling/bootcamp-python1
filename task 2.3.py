AGE_0 = 0 
AGE = 17

valid = False
while not valid:
    user_age = int(input("Please enter your age in years: "))
    if user_age >= AGE:
        valid = True
        print(str(user_age) + " is old enough to drive in the UK.")
    elif user_age > AGE_0 and user_age < AGE:
        valid = True
        print(str(user_age) + " is not old enough to drive in the UK.")
    else:
        print("Invalid input.")
