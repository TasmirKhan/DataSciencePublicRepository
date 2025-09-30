print("Functions Arguments (Deep dive)")

def posArg(name,age):
    print(f"Hii {name}, Your age is {age}")

def keyArg(age =0, name="None"):
    print(f"Hii {name}, Your age is {age}")

def defArg(name = "Guests"):
    print(f"Hello {name}")

def arbArg(*args):
    return sum(args)

print(arbArg(1,2,3,4,5,6))
print(defArg())

def largest(*args):
    return max(args)

print("Practice:-")
print(largest(2,32,3,24,2,42,4,23,2,354,53,4,43,44,24,4,23,4,42,5))

def words(*kwords):
    return " ".join(kwords)

print(words("hello","dear","i","am","here"))

def info(**kwargs):
    for key , values in kwargs.items():
        print(f"{key}:{values}")
    return 
print(info(name="Ali",age = 19,marks = 99))

print("Task work:")
students = {}

def marks(*args):
    for i in range(len(args)):
        students[i+1] = args[i]


def stdinfo(**kwargs):
    for key,values in kwargs.items():
        students[key]  = values

marks(1,2,3,4,34,21,45)
stdinfo(name ="Sam",age = 25,dept= "CSE")
print(students)

def shopping_cart(**kwargs):
    sum = 0
    for key,values in kwargs.items():
        print(f"{key} = {values}")
    for i in kwargs.values():
        sum +=i
    return sum

print("total bill: ",shopping_cart(rice = 43,wheat = 23,bread = 35))