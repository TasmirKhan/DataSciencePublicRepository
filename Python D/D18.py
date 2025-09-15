print("Pattern printing program:")

def patternPrinting():
    x = int(input("Enter a number: "))

    print("Right Triangle")
    for i in range(1,x+1,1):
        for i in range(i):
            print("*",end="")
        print()

    print("Inverted Right triangle:")
    for x in range(x,0,-1):
        for i in range(x):
            print("*",end="")
        print()

def noprint():
    x = int(input("Enter the number"))
    print("Number Triangle:")
    for j in range(1,x+1):
        for k in range(1,j+1):
            print(k,end="")
        print()


def tablegrid():
    print("Mult. table grid")
    i =1
    count =1
    while(i<=10):
        while(count<=10):
            print(f"{count*i:4}",end=" ")
            count+=1
        print()
        i+=1
        count =1
    
def pyramidPattern():
    n = int(input("Print the number of rows you wanted"))
    
    if(n>0):
        for i in range(n):
            for j in range(2*n):

                if (j>=n-i and j<n+i):
                    print("*",end="")
                elif(j>=n+i and j<=n+i):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

patternPrinting()
noprint()
tablegrid()
pyramidPattern()