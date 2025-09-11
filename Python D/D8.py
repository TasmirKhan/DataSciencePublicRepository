print("""Marks analyzer""")
report = []
j=1
while(j<=5):
    # x = int(input(f"Enter the marks of the Subject {j} "))
    # report.append(x)
    report.append(int(input()))
    j+=1

print("Marks of the student:- ", end="")
for num in report:
    print(num, end = " ")

print("\n",sum(report))
print(sum(report)/len(report))
for i in range(5):
    print(f"Subject{i+1}, position = {i+1}, Marks = ", report[i])

print("Enter any number:- ")
x = int(input())
if x in report:
    print(f"found at index {report.index(x)}")
else:
    print("Not exist")


report.sort(reverse=True)
for item in range(len(report)):
    print(report[item], end=" ")