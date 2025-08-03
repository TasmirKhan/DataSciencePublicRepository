print("Here in this program we are going to learn about the tuples")
tuple = (1,2,3,4,5,6,"Tasmir Khan", "Java")
print("Tuples are immutable and are as like as lists")
print(tuple)
print(tuple[3])
print(tuple.count("Tasmir Khan"))
print(tuple.index("Java"))
print(len(tuple))
if "Java" in tuple:
    print("Java present in the given tuple")
else:
    print("Java is not present in the given tuple")

tuple1 = tuple[0:7]
print(tuple)
print(tuple1)