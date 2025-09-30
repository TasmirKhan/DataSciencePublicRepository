str = "I am coming to be the best and i know i will become the best"
uniqchar = {ch for ch in str}
uniqvwl = {ch for ch in str if ch in "aeiouAEIOU"}
sqset = {n**2 for n in range(1,11)}
words = {ch for ch in str.split()}

print("SET ANALYZER PROGRAM: ")
a = input("Enter a sentence : ")
VWLltrs = {ch for ch in a if ch in "aeiouAEIOU"}
wrds = {ch for ch in a.split()}
constants = {ch for ch in a if ch  not in "aeiouAEIOU"}

print(f"{VWLltrs}\n{wrds}\n{constants}")
n = int(input("Enter a number:"))
multthree = {x for x in range(n+1) if x%3==0}
multfive = {x for x in range(n+1) if x%5==0}
common = multfive.intersection(multthree)
print(f"{multthree}\n{multfive}\n{common}")

print("Extras")
lst = ["Alice","Sam","Jack","David","Joseph"]
setlst = {ch[0] for ch in lst }
primeset = {x for x in range(2,n+1) if all(x%i!=0 for i in range(2,int(x**0.5)+1))}
print(f"{setlst}\n{primeset}")

