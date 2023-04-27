## Task 3.6
##Write a program which asks the user to enter a series of sentences. The program should keep
##asking for sentences until user types "" (the empty string, i.e., they just press enter). Once the
##user has typed "" the program should output the total number of words that were entered and
##the total number of vowels.
##Assume that any substring separated from others by spaces on both sides (or one side if it is at
##the start/end of the string) is a word.

sentences = str(input("Please enter a sentence: "))

VOWELS = "aeiouAEIOU"
vowels_list = []
word_counts = 0
vowel_counts = 0

while sentences != "": #if string is not empty enter the while loop
    word_counts = word_counts + len(sentences.split(" ")) # separated the strings and count
    
    for i,j in enumerate(sentences):
        if j in VOWELS:  # if a character is vowels, add it to the list then count the length of list
            vowels_list.append(j)
    vowel_counts = len(vowels_list)
    
    sentences = str(input("Please enter a sentence: ")) # ask user to input another sentence

print("Word counts are: " + str(word_counts))
print("Vowel_counts are: " + str(vowel_counts))
            
        
    
