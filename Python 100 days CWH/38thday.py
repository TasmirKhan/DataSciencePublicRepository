print("Here in this program we will learn about the custom errors in python.")
# x = int(input("Enter a Number."))
# if(x<0):
#     raise ValueError("Negative value not allowed! ERROR!")
#     print("ok")
# else:
#     print("Value is ", x)
# print("Enter another value")
# y = int(input("Enter the other value. "))
# print("the other value is ", y)
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    def __init__(self, value, message="Negative numbers are not allowed"):
        self.value = value
        self.message = message
        super().__init__(self.message)

# Using the custom error
def square_root(num):
    if num < 0:
        raise NegativeNumberError(num)
    return num ** 0.5

try:
    x = int(input("Enter the number to find the square root of it."))
    print(square_root(x))
except NegativeNumberError as e:
    print(f"Error: {e}")
