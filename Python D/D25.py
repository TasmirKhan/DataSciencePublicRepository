print("Welcome in Student Management App")
import json
import os

FILE_NAME = "students.json"

# Load data from file if exists
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# Save data to file
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student(students):
    name = input("Enter student name: ").strip()
    if name in students:
        print("Student already exists!")
        return
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))
    students[name] = {"age": age, "marks": marks}
    save_data(students)
    print("Student added successfully!")

# View all students
def view_students(students):
    if not students:
        print("No students available.")
        return
    for name, details in students.items():
        print(f"Name: {name}, Age: {details['age']}, Marks: {details['marks']}")

# Search student by name
def search_student(students):
    name = input("Enter name to search: ").strip()
    if name in students:
        details = students[name]
        print(f"Found -> Name: {name}, Age: {details['age']}, Marks: {details['marks']}")
    else:
        print("Student not found.")

# Delete student
def delete_student(students):
    name = input("Enter name of student to delete: ").strip()
    if name in students:
        del students[name]
        save_data(students)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Student report
def student_report(students):
    if not students:
        print("No data available for report.")
        return
    marks = [details['marks'] for details in students.values()]
    print("---- Student Report ----")
    print(f"Total Students: {len(students)}")
    print(f"Total Marks: {sum(marks)}")
    print(f"Average Marks: {sum(marks)/len(marks):.2f}")
    print(f"Max Marks: {max(marks)}")
    print(f"Min Marks: {min(marks)}")

# Menu
def menu():
    students = load_data()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Show Student Report")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            student_report(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run program
if __name__ == "__main__":
    menu()
