print("my own program:")
student = dict()

def menu():
        print("It's a Menu Driven Student Management App: ")
        print("""1.Add Students(name,age,marks)\n2.View All Students\n
              3.Search student by name\n4.Show student report(total,avg.,max,min)
              \n5.Exit""")
     
def addStudents():
        name = input("Enter the student name: ")
        age = int(input("Enter the student age: "))
        marks = int(input("Enter the marks of the student:"))
        student[name] = {"age":age,"marks":marks}
        # student["age"] = y
        # student["marks"] = dict()
        # for i in range(5):
        #     z = int(input(f"Enter marks of the subject {i+1}:"))
        #     student["marks"][i+1] = z
        

def viewStudent():
        for i,j in student.items():
            print(f"{i} : {j}")
    
def searchByName():
        s = input("Enter the name: ")
        if s in student.keys():
            print("Student exist")
            print(student[s])
    
def report():
        total = sum(student["marks"])
        avg = sum(student["marks"])/len(student["marks"])
        max = max(student["marks"])
        min = min(student["marks"])
        print(f"Total = {total}\nAverage = {avg}\nmax = {max}\nmin = {min}")
        
def deleteStudent():
        del student

menu()   
addStudents()
viewStudent()
searchByName()
report()


