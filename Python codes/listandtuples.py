print("Program for list and tuples")
marks = ["Tasmir", 26 , "Arhaana", 21.5]
print(marks)
print(marks[0], marks[2])
marks[3]= 20
print(marks)
print("length of marks list is", len(marks))
print(marks[:3])

marks.append("Abbas")
print(marks)
list = [2,3,2,5,1,6,3,9]
list.append(50)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
list.insert(3,999)
list.remove(5)
list.pop(6)
print(list)