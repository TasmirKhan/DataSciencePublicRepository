print("Sets in Python")
m = {"sharique","aman","Raahil","tasmir","zahid","saad","Nosin"}
y ={"sharique","tasmir","zahid","sarthak","sheetal","sharyu","sanjana","Shareen"}
z = m.intersection(y)
print(m)
print(y)
print(*m)
print(*y)
print(m.union(y))
print(m.intersection(y))
print(m.difference(y))
print(y.difference(m))
print(m.symmetric_difference(y))
print(y.symmetric_difference(m))

print("Shareen" in y)
print("Nosin" in m)

print(z.issubset(m))

list = [1,2,3,2,1,2,3,4,22,3,4,2,3,4]
print(list)
list = set(list)
print(list)

