print("Word and Number Analyzer")

def wordAnalyzer():
    str1 = "The day belong to no one the night belong to no one the sky is ours and our wings are free to fly"
    ext = [x for x in str1.split(" ") if x[0] in "aeiouAEIOU"]
    cntlt = [ len(x) for x in str1.split(" ") ]
    ulst = [x.upper() for x in str1.split(" ")]
    print(f"{ext}\n{cntlt}\n{ulst}")

def numberAnalyzer():
    x = int(input("Enter any no."))
    sq = [a**2 for a in range(1,x+1)]
    even = [a for a in range(1,x+1) if a%2==0]
    prime = [a for a in range(2,x+1) if all( a%i!=0 for i in range(2,int(a**0.5)+1))]
    print(f"{sq}\n{even}\n{prime}")

wordAnalyzer()
numberAnalyzer()