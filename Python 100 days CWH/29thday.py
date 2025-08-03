# def square(n):
#   '''Takes in a number n, returns the square of n'''
#   print(n**2)
# square(5)
# print(square.__doc__)

def add(a,b):
    '''ADDS Two number a and b'''
    return a+b
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print(add(x,y))
print(add.__doc__)