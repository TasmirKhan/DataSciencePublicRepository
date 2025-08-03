print("Here we are going to use different types of arguments in the functions")

def firstfunction(a=0, b=0,c=1):
    mean = (a*b*c)/(a+b+c)
    return mean
def average(*numbers):
    sum =0
    for i in numbers:
        print(i)
        sum = sum+i
    return sum/len(numbers)

average(1,2,3,4,5,6)
print(firstfunction(2,3))
print(average(1,2,3,4,5))