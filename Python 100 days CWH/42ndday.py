print("In this program we are going to see the use of enumerate in python ")
print("Enumerate is used to track the elements of a container along with it's elements.")
s = [1,2,3,4,5,1,2,3,4,5]
# for index, element in enumerate(s):
#     print(index , "->", element)

for index, element in enumerate(s, start=5):
    print(index, "->",element)