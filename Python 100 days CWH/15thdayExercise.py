print("Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program")
import time
timestamp = time.strftime('%H:%M:%S')
timestampp = time.strftime('%H%M%S')
print(timestamp)
print(timestampp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

current_Hour = time.localtime().tm_hour
print(current_Hour)
# Good Morning → 05:00 - 11:59
# Good Afternoon → 12:00 - 17:59
# Good Evening → 18:00 - 20:59
# Good Night → 21:00 - 04:59
rt = int(current_Hour)
if(rt>=5 and rt<12):
    print("Good Morning")
elif(rt>=12 and rt<18):
    print("Good AfterNoon")
elif(rt>=18 and rt<21):
    print("Good evening")
elif(rt>=21 or rt<5):
    print("Good Night")

print("Thank You!")