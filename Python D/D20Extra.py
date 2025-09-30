print("Hello pytu")
n = int(input("Enter a number: "))
nlst = [x for x in range(1,n+1)]
oddlst = [x for x in range(1,n+1) if x%2!=0]
print("Enter 3 random words: ")
wlst = [input() for _ in range(3)]
wlst1 = [ch.upper() for ch in wlst ]
sentence = "i am the only one here to be the chosen one and no one should dare to compete me,Inshallah I will be the first billionaire of my family."
lstc = [ch[0] for ch in sentence.split(" ")]
sqlst = [x**2 for x in range(1,n+1)]
evenlst = [x for x in range(1,n+1) if x%2==0]
vlst = [ch for ch in sentence if ch in "aeiouAEIOU"]
z = 19
mult = [i*z for i in range(1,11)]
twoD = [(x,y) for x in range(1,10) for y in range(1,3)]

print(f"{nlst}\n{oddlst}\n{wlst}\n{wlst1}\n{lstc}\n{sqlst}\n{evenlst}\n{vlst}\n{mult}\n{twoD}")
