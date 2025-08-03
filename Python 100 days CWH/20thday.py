print("Here we are going to learn about the functions in python")

def calculatemean(a,b):
    mean = (a*b)/(a+b)
    # print(mean)
    return mean


def calculatelesser(a,b):
    if(a<b):
        return a
    if(a>b):
        return b

print(calculatelesser(3,5))
print(calculatemean(3,5))
