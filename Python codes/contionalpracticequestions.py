#Program to check whether a given no. is even or odd
no = int(input("Enter your number "))
if(no%2==0):
    print("Even number")
else:
    print("odd number")

a = int(input("Enter first number "))
b = int(input("Enter second number"))
c = int(input("Enter third number "))

if(a>b):
    if(a>c):
        print(a,"is greatest")
    else:
        print(c,"is greatest")

elif(b>a):
    if(b>c):
        print(b,"is greatest")
    else:
        print(c,"is greatest")

x = int(input("Enter the number to find whtether it is divisible by 7 or not"))
if(x%7==0):
    print(x,"is divisible by 7")
else:
    print(x,"is not divisible by 7")
    print("reminder of the", x, "when divided by 7 is", x%7)


p = float(input("Enter 1st number"))
q = float(input("Enter 2nd number"))
r = float(input("Enter 3rd number"))
s = float(input("Enter 4th number"))
if(p>=q and p>=r and p>=s):
    greatestnumber = p
elif(q>=r and q>=p and q>=s):
    greatestnumber = q
elif(r>=p and r>=q and r>=s):
    greatestnumber = r
elif(s>=p and s>=q and s>=r):
    greatestnumber= s

print("Greatest number is ", greatestnumber)
