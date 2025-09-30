import string
print("Dictionary Comprehension")
sentence = "I will achieve what i am coming for."
cubedict = {x:x**3 for x in range(1,11)}
chdict = {ch:ord(ch) for ch in string.ascii_letters}
wrdfreq = {word:sentence.split().count(word) for word in sentence.split()}

print(f"{cubedict}\n{chdict}\n{wrdfreq}")

print("Dictionary Builder program:")
sqdict = {x:x**2 for x in range(1,10)}
a = input("Enter word: ")
letterlst = {ch:a.count(ch) for ch in a}
print(f"\n\n{sqdict}\n{letterlst}")

specialdict = {x:{y for y in range(1,11) if y%x==0} for x in range(1,5)}
sentlen = {x:len(x) for x in sentence.split()}

print(specialdict)
print(sentlen)