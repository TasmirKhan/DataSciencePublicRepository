print("Here we are going to make factorial and fibonacci program with the help of recursion.")
x = int(input("Enter the number you want to find factorail of: "))

def factorial(a):
    if(a==0 or a==1):
        return 1
    else:
        return a*factorial(a-1)
    
print( "Factorial using recursion reached - ",factorial(x))
