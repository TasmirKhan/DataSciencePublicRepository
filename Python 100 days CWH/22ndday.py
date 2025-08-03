print("Here we are going to learn about the list")
list = [1,2,3,"Tasmir Khan", "hello", 1.2 ,3.4]
print(list)
print(list[3])
print("indexing is started from 0", list[0])
print(list[-2])
print("length of the list is ", len(list))
if 3 in list:
    print("Number Exists")
if "Tasmir Khan" in list:
    print("Name Exists")

print(list[1:len(list):2])
