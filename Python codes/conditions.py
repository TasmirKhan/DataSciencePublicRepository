print("Here we are going to make a program for the students results\nusing conditional statements\nhere proper indentation is required")
marks = int(input("Enter marks of the student "))
if(marks>100 or marks<0):
    print("invalid")
elif(marks>=90):
    print("A")
elif(marks>=80):
    print("B")
elif(marks>=70):
    print("C")
elif(marks>=60):
    print("D")
elif(marks>=50):
    print("E")
else:
    print("Fail")

