print("Enter your three favourite superstar names")
n1= input()
n2= input()
n3= input()
list = []
list.append(n1)
list.append(n2)
list.append(n3)
print(list)

print("To check a list contain a palindrome of elements")
list2 = [1,2,3,4,5,6,7,4,3,2,1]
list3 = list2.copy()
list3.reverse();
if(list2 == list3):
    print("True palindrome")
else:
    print("Non palindrome")

tup= ("C","D","A", "A", "B","B", "A")
print("Students with A Grade are", tup.count("A"))
srt = ["C", "D", "A", "A", "B", "B", "A"]
print("sorted srt is ", srt.sort())
print(srt)