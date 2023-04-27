user_input = input("Please enter the temperature: ")
temp_int = int(user_input[0:-1])
solid_celsius = 0
liquid_celsius = 100

solid_fahrenheit = 32
liquid_fahrenheit = 212


if user_input[-1] == "c" or user_input[-1] == "C":
    if temp_int < solid_celsius :
        print("Water is solid at this temperature")
    elif temp_int < liquid_celsius :
        print("Water is liquid at this temperature")
    else :
        print("Water is gas at this temperature")
elif user_input[-1] == "f" or  user_input[-1] == "F":
    if temp_int < solid_fahrenheit :
        print("Water is solid at this temperature")
    elif temp_int < liquid_fahrenheit:
        print("Water is liquid at this temperature")
    else :
        print("Water is gas at this temperature")


