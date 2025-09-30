print("Working with CSV files: ")

# A plain text file where data is separated  by commas.
print("Reading CSV files")
import csv

with open("data.csv","a") as f:
     f.write("This is a csv file")

with open("data.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("data.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Alice",29,"NYC"])
    writer.writerow(["Bob",30,"London"])

print("Using DictReader and DictWriter (More Powerful)")
import csv 
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"],row["City"])

print("Practice: ")
with open("info.csv","w") as f:
    f.write("This is student information file")
    writer = csv.DictWriter(f)
    for row in writer:
        name = input("Student name:")
        age = int(input("age:"))
        marks = int(input("marks:"))
        row["name"] =name 
        row["age"] = age
        row["marks"] = marks

    
    


