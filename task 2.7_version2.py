time_input = input("Please enter a time in hh:mm:ss format: ")
hour = int(time_input[0:2])
minute = int(time_input[3:5])
second = int(time_input[6:8])


# Set new time, incrementing seconds
newHour = hour
newMinute = minute
newSecond = second + 1

# If seconds become 60, reset seconds and increment minutes
if newSecond == 60 :
    newSecond = 0
    newMinute = newMinute + 1

# If minutes become 60, reset minutes and increment hours
if newMinute == 60 :
    newMinute = 0
    newHour = newHour + 1

# If hours become 24, reset hours
if newHour == 24 :
    newHour = 0 

print(str("%02d" % newHour) + ":" + str("%02d" % newMinute) + ":" + str("%02d" % newSecond))

