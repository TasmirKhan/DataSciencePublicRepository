print("Here we are going to learn about OOPs in python")
# Object Oriented Programming in Python
class Student:
    def __init__(self, name, marks, age, rollno):
        self.name = name
        self.marks = marks
        self.age = age
        self.rollno = rollno
        print("New Student info. added to the database.....")
    def display(self):
        print(self)
        print("Name: ", self.name)
        print("Marks: ", self.marks)
        print("Age:", self.age)

s1 = Student("Tasmir Khan", 100, 24, 230)
print(s1)
# print(s1.name)
# print(s1.rollno)
s1.display()

s2 = Student("Aman", 95,23,205)
s2.display()