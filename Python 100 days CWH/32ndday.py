print("set methods in python")
Tasmir = {7.67, 25000, "Indore"}
if 8.5 in Tasmir:
    print("yes 8.5 present")
else:
    print("No")

Tasmir.add("Khan")
print(Tasmir)
Tasmir.remove("Indore")
print(Tasmir)
# Tasmir.remove("Car")
Tasmir.discard("Car")
print(Tasmir)
Tasmir.clear()
print(Tasmir)
# add(elem)
# Adds element elem to the set.

# update(iterable)
# Adds all elements from the given iterable (e.g., list, set, tuple) to the set.

# remove(elem)
# Removes element elem from the set. Raises a KeyError if elem is not present.

# discard(elem)
# Removes element elem from the set if it exists. Does nothing if elem is not present.

# pop()
# Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

# clear()
# Removes all elements from the set, leaving it empty.

# union(*others) or | operator
# Returns a new set with elements from the set and all others. For example, set1.union(set2) or set1 | set2.

# intersection(*others) or & operator
# Returns a new set with elements common to the set and all others. For example, set1.intersection(set2) or set1 & set2.

# difference(*others) or - operator
# Returns a new set with elements in the set that are not in the others. For example, set1.difference(set2) or set1 - set2.

# symmetric_difference(other) or ^ operator
# Returns a new set with elements in either the set or other but not in both. For example, set1.symmetric_difference(set2) or set1 ^ set2.

# issubset(other) or <= operator
# Returns True if every element in the set is in other.

# issuperset(other) or >= operator
# Returns True if every element in other is in the set.

# copy()
# Returns a shallow copy of the set.