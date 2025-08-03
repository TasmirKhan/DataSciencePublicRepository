print("Welcome to the 14th day of 100 days of Python.")
print("Here we are going to learn the use of if - else and all terms related to them.")
a = int(input("Enter your Age: "))
if(a>=18 and a<100):
    print("You can drive and you can vote")
elif(a<18 and a>0):
    print("You can't drive and you can't vote")
else:
    print("Invalid Input")