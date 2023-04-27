##Task 3.4
##Write a program that reads a line of input as a string and outputs:
##1. Only the uppercase letters in the string.



input_string = str(input("Please enter a sentence: "))

capital_letter = ""
for i in input_string:
    if i.isupper():
        capital_letter = capital_letter + str(i) + " "
        
print("The capital letters are: " + capital_letter, end="")

print(" ")

##2. Every second character of the string.
#Method 1
for i in range(1,len(input_string), 2):
    print(input_string[i], end="")
print(" ")    

#Method 2
second_character = ""
for i,j in enumerate(input_string):
    if (i+1) % 2 == 0:
        second_character = second_character + j
print("Every second character of the string are: " + second_character, end="")

print(" ")

##3. The positions of all vowels in the string.
#Method 1
vowels_position = []
vowels_list = "aeiouAEIOU"
for i,j in enumerate(input_string):
    if j in vowels_list:
        vowels_position.append(i)
        
print("The position of vowels are: ", vowels_position, end="")
print(" ")

#Method 2

for i in input_string:
    if i in vowels_list:
        print( input_string.index(i), end="")



