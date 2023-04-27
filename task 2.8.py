user_input = str(input("Please enter a word to check whether it is palindrome: "))
pointer1 = user_input[0]
pointer2 = user_input[-1]
count = 0
flag = len(user_input)//2
valid = True

while count < flag: 
    if pointer1 == pointer2:
        count = count + 1
        pointer1 = user_input[0 + count]
        pointer2 = user_input[-1 - count]
            
    else :
        print(user_input + " is not a palindrome.")
        valid = False
        break
    
if valid == True:
    print(user_input + " is a palindrome ")
