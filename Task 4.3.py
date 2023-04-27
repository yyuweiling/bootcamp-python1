def main():
    print(max_list([3,7,4,4,2,5]))
    print(max_list([38,27,42,14,25,54]))
    print(max_list([5,7,14,3,6]))
    

def max_list(lst):
    largest = lst[0]
    for i in range(1,len(lst)):
        if lst[i] >= largest:
            largest = lst[i]
    
    return largest
        
          
        

main()
