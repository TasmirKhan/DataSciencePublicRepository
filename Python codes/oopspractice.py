print("This is a practice code")
# create a student class that take name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.
class Student:
    def __init__(self):
        self.name = input("Enter the name of the student: ")
        self.marks1 = int(input("Enter the marks of 1st subject:"))
        self.marks2 = int(input("Enter the marks of 2nd subject:"))
        self.marks3 = int(input("Enter the marks of 3rd subject:"))
    def avg(self):
        print("Average of marks of the student is:")
        return (self.marks1+self.marks2+self.marks3)/3
    def normal(self):
        print("This is a normal method")
    
s1 = Student()
# s1.avg()
print("Name of the student is ", s1.name)
print(s1.avg())
# s1.normal() without giving the self  Traceback (most recent call last):
#   File "/workspaces/codespaces-blank/Python codes/oopspractice.py", line 19, in <module>
#     s1.normal()
# TypeError: Student.normal() takes 0 positional arguments but 1 was given
s1.normal()