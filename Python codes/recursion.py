print("Program to show the power of recursion in Python")


def show(n):
    if (n==0):
        return 
    print(n)
    show(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

def sumofn(n):
    if n==0:
        return 0
    else:
        return n+sumofn(n-1)

def showlist(n,x=0):
    if(x==len(n)):
        return 
    print(n[x])
    x+=1
    showlist(n,x)


list = [1,3,2,5,3,7,6]
n= int(input("Enter the number:"))   
show(n)
print("Factorial of",n,"=",factorial(n))


print("Practice Questions Program on recursion")
print("sum of the first",n,"natural no.=",sumofn(n))
print("Elements of the list are", showlist(list))

