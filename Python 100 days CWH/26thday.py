print("Exercise 2 solutions")
import time

current_time = time.strftime("%H:%M:%S")
print("Current time according to London timezone is:- ",current_time)
t = int(time.strftime("%H"))
if t>=0 and t<12:
    print("Good Morning")
if t>=12 and t<17:
    print("Good Afternoon")
if t>=17 and t<0:
    print("Good Night")