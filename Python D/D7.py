print("This is a program for the list: ")
list = []
print("Enter add to add items if don't want to add write 'quit'")
print("Enter remove to remove items from the list ")
while(True):
    x = input("")
    x = x.strip()
    if x == "quit":
        break
    elif x == "remove":
        y = input("Enter the item to be removed ")
        y = y.strip()
        list.remove(y)
    else:
        list.append(x)
list.sort()
print(list)
print(len(list))
list.sort(reverse= True)
print(list)
lst = sorted(list)
print(lst)
print(list)

unique = (set(lst))
print(unique)