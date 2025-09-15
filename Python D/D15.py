print("Student record system:")

def addStudents(record):
    x=int(input("Enter the number of the students to be added:"))
    while(x>0):
        y = int(input("Enter the id of the student: "))
        n1 = input("Enter name of student:")
        a = int(input("Enter age of the student:"))
        c1  = input("Enter course of the student:")
        record[y] = (n1,a,c1)
        x-=1
    

def removeStudents(record):
    x=int(input("Enter the number of the students to be removed"))
    while(x>0):
        y = int(input("Enter the id of the student: "))
        if y in record:
            del record[y]      
        x-=1

def displayStudents(record):
    for key ,values in record.items():
        print(f"{key}: {values}")

def showUniqueCourses(record):
    course= set()
    for values in record.values():
        course.add(values[2])
    print("Uniques courses:- ")
    for x in course:
        print(x,end = " ")

record = {
    2302026:("Sharique Khan",20,"B.tech-CSE"),
    2302025:("Shareen Khan",20,"B.tech-CSE"),
    2301940:("Tasmir Khan",22,"B.tech-CSE (Artificial Intelligence)"),
    2301941:("Nosin Khan",22,"Physiotherapist"),
    2302024:("Sheetal Ghadiya",21,"B.tech-CSE")
    }
record[2302023] = ("Tanu",20,"B.tech-CSE")
record[2302020] = ("Sarthak ",18,"B.tech-CSE")
del record[2302024]
record.pop(2302023)

while(True):
    print("Enter:-\n1.Add Students\n2.Remove Students\n3.Display all students\n4.Show Unique Courses\n5.Exit")
    t = int(input())
    if(t==1):
        addStudents(record)
    elif(t==2):
        removeStudents(record)
    elif(t==3):
        displayStudents(record)
    elif(t==4):
        showUniqueCourses(record)
    elif(t==5):
        print("Thank You! Exiting......")
        break
    else:
        print("Invalid Input!\nTry Again")


# print(*record.items())

# print("display via loops")
# for key,values in record.items():
#     print(f"{key} : {values}")


# name =[]
# age = []
# course = []

# #show unique courses
# for values in record.values():
#     name,age,course 