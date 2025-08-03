def average(a,b,c):
    print((a+b+c)/3)
    return (a+b+c)/3

def mult(a,b):
    print(a*b)
    return a*b

def factorial(a=1):
    i=1
    temp =1
    while i<=a:
        temp = temp*i
        i+=1
    print("Factorial of",a,"is",temp)


def currencychange(a=1):
    print(a,"dollar =",a*85.50)
    return a*85.50

def printlist(a):
    temp = len(a)
    print("\nElements of the list are:-")
    for el in range(0,temp):
        print(a[el])

def lenoflist(a):
    print( "Length of the given list is",len(a))
    return len(a)
a =20
b=40
c=5
list = [11,4,2,5]
average(a,b,c)
mult(a*b,c)
factorial(c)
currencychange()
lenoflist(list)
printlist(list)