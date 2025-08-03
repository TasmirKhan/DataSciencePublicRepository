print("We are going to make a dictionary")
x = int(input("Enter your car no."))
dictionary = {
     "name" : "Tasmir khan",
     "Age " : 23,
     "Salary" : "100k dollars",
     "list" : ["java", "python", "DSA", "Web development"],
     "tuple" : ("dictionary", "set")

}

print("The dictionary ++++")
print(dictionary)

print(" ")
print(dictionary["name"])
print(dictionary["list"])

nested_dict = {
    "student": "Sameer",
    "Score" : {
        "phy" :99,
        "chem" :94.58,
        "Math" : 99
    },
    "pass"  : True
}

print(" ")
print("Nested dictionary")
print(nested_dict)
print(nested_dict["pass"])
print(nested_dict["Score"]["phy"])

print(" ")
print("Here we are going to build a null dictionary and add key and their values in it")
null_dict = {}
null_dict["key1"] = "office"
print(type(null_dict))
print(null_dict,"\n")

print("nested keys", nested_dict.keys())
print