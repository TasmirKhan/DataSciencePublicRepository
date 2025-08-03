print("Here we are going to learn and use static method in python")
# Static method is a method that bound to the class not the object of the class.


class student:
    name = "Anonymus"
    @staticmethod
    def school():
        print("This is a static method of the class student")
        print("Name of the student will be showed if it's private is :", student.name)

    def classes(self):
         print("this is a non static or normal method")

    def __init__(self, name, batch, rollno, section):
        self.name = name
        self.batch = batch
        self.rollno = rollno
        self.section = section
        
    def display(self):
            print("name = ", self.name)
            print("batch =", self.batch)
            print("rollno =", self.rollno)
            print("section = ", self.section)    

s1 = student("aman", "2020", 123, "r2")
s1.school()
s1.display()
s1.classes()
student.school()