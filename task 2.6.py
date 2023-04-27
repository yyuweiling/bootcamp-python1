MIN = 3
MAX = 10
box_replication = "*"
empty= " "
valid = False

while not valid:
    size_input = int(input("Please enter the size of box: "))
    if size_input >= MIN and size_input <= MAX :
        valid = True
        filled_input = str(input("Please state if you want the box to be filled or not: "))
        box_filled = box_replication * size_input 
        if filled_input == "filled" :
            print((box_filled + "\n")*size_input)
        elif filled_input == "not filled":
            box_not_filled = box_replication + empty * (size_input -2) + box_replication
            print(box_filled + "\n" + (box_not_filled + "\n")* (size_input -2)+ box_filled )
        
    else :
        print("Please enter an integer between 3 and 10")

