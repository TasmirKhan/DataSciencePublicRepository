print("Functions basics:")
import math

def fact(x,y):
    r1,r2=1,1
    for i in range(1,x+1):
        r1 = r1*i
    print(f"Factorial of {x}",r1)

    for i in range(1,y+1):
        r2 = r2*i
    print(f"Factorial of {y}",r2)
def sq():
    x = int(input("Enter the number:"))
    print(f"{x} : {x**2}")
    return x**2

def sum(a,b):
    return a+b

def diff(a,b):
    return abs(a-b)

def mult(a):
    for i in range(1,11):
        print(f"{i*a}")
    return

def countVowels(str):
    for ch in str:
        if ch in "aeiouAEIOU":
            print(ch,end=" ")

def primes_upto(n):
    return [num for num in range(2, n+1) 
            if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

def calculator():
    x = int(input("Enter first number:"))
    y = int(input("Enter the second number:"))
    operator = input("Enter the operator to perform operation(+,-,*,/,fact,isprime):")
    match operator:
        case "+":
            print(x+y)        
        case "-":
            print(x-y)
        case "*":
            print(x*y)
        case "/":
            print(x/y)
        case "fact":
           fact(x,y)
        case "isprime":
            primes_upto(x)
        
sq()
print(sum(12,54))
print(diff(56,23))
mult(7)
countVowels("sharique/shareen")

