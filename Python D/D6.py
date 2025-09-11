import re
print("This is a Playground program")
str = input("Enter the Sentence:\n")
print("length of the string", len(str),str.upper(),str.lower(), str[0],str[-1], str.strip(),str.replace(" ","-"))
print("Reverse of the string:- ", str[::-1])
str2 = input("Enter the word")
if str2 in str:
    print(str.find(str2))
    print(str.rfind(str2))
    print(str.index(str2))
    print([m.start() for m in re.finditer(str2, str)])
    