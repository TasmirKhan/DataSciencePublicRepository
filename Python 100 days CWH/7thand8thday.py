print("In this program we are going to do an Exercise for creating Calculator")
a = (int(input("Enter first number: ")))
b = int(input("Enter second number: "))
print("Enter 1 for addition \n2 for subtraction\n3 for divisionn\n4 for multiplication\n5 to find square of the numbers")
c = int(input())
if(c==1):
    print(a+b)
elif(c==2):
    print(a-b)
elif(c==3):
    print(a/b)
elif(c==4):
    print(a*b)
elif(c==5):
    print(a**2)
    print(b**2)


