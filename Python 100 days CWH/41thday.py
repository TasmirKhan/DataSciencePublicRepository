print("In this program of code we are going to see that the use and work of short hand if else.")
try:
    a = int(input("Enter the number first: "))
    b = int(input("Enter the number second: "))
    print("First element is bigger.") if (a>b) else print("Second element is big")
finally:
    print("value_if_true if condition else value_if_false")