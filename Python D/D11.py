print("Tuple in python")
tple = (1,2,3,4,5,6)
tple2 = (2,)
print(type(tple), tple[2])
print(type(tple2))
print(tple)
print(*tple)

print(tple.count(2), tple.index(4))

a,b,c,d,e,f = tple
print(a,f)

print("\n\nStudent info. using Tuples:-")
details = ("Sharique", 21,"B.tech CSE-AI")
name, age, course = details
print(f"{name} \n{age}\n{course}")

course_details = ("CSE", "MECHANICAL","CIVIL", "ELECTRICAL")
x = input("Enter course name: ")
if x in course_details:
    print("Exist")
else:
    print("Not exist")

money = (100,200, 500, 1000, 2000)
print(max(money), min(money), sum(money))
list = list(money)
print(money)
print(list)
money2 = tuple(list)
print(money2)