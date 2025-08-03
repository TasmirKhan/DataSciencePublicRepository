print("Dictionary in Python")
keys = {'one', 'two','three'}
values = ['I','II','III']
print("A dictionary in Python is a collection of key-value pairs where each key is unique. Dictionaries are mutable, meaning you can change them after creation.")
dict1= {'Name':'Tasmir Khan','Semester': 4 ,'Specialization': 'Artificial Intelligence'}
print(dict1)
print(dict1.pop('Semester'))
print(dict1.fromkeys(keys,values))
print(dict1)

# print("Dictionary in Python")

# # Define keys and values
# keys = {'one', 'two', 'three'}
# values = ['I', 'II', 'III']

# print("A dictionary in Python is a collection of key-value pairs where each key is unique. "
#       "Dictionaries are mutable, meaning you can change them after creation.")

# # Create a dictionary
# dict1 = {'Name': 'Tasmir Khan', 'Semester': 4, 'Specialization': 'Artificial Intelligence'}
# print("Original dictionary:", dict1)

# # Remove the key 'Semester' and print its value
# removed_value = dict1.pop('Semester')
# print("Popped 'Semester':", removed_value)

# # Create a new dictionary using fromkeys.
# # This will not affect dict1.
# new_dict = dict.fromkeys(keys, values)
# print("New dictionary created with fromkeys:", new_dict)

# # Print dict1 again to show it remains unchanged after fromkeys (aside from the earlier pop)
# print("Dictionary after pop:", dict1)
