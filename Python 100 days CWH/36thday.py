print("Here in this program we will see\nTry-Except blocks use")
try:
    x = int(input("Enter a number:"))
    num = [1,2]
    print(num[x])
except ValueError:
    print("Entered value is not an integer")
except IndexError:
    print("Index Not found")