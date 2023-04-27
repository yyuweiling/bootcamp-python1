time_input = input("Please enter a time in hh:mm:ss format: ")
hh = int(time_input[0:2])
mm = int(time_input[3:5])
ss = int(time_input[6:8])

if ss >= 0 and ss < 59 :
    ss = ss + 1
    print(str("%02d" % hh) + ":" + str("%02d" % mm) + ":" + str("%02d" % ss))
    
elif ss == 59 and mm == 59:
    hh = hh + 1
    print(str("%02d" % hh) + ":" + str("%02d" % 0) + ":" + str("%02d" % 0))
 
elif ss == 59 and mm != 59:
    mm = mm + 1
    print(str("%02d" % hh) + ":" + str("%02d" % mm) + ":" + str("%02d" % 0))

else :
    print("please enter correct format: ")
    


    


            
