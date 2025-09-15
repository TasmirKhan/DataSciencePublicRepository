print("Looping with list and strings")

def practice():
   
    str = "Tasmir Khan"
    for ch in str:
        if ch in "aeiouAEIOU":
            print(ch, end=" ")
    print()

    lst = [12,3,4,3,45,6,2]
    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    print(lst)
    print(sum(lst))
    
    dict1 = {}
    for ch in str:
        if ch in dict1:
            dict1[ch] = dict1[ch]+1
        else:
            dict1[ch] = 1
    print(dict1)

def wordAnalyzer():
    x = input("Enter the word:")
    vwl =[]
    count =0
    for ch in x:
        print(f"{ch} : {x.index(ch)}", end=" " )
        if ch in "aeiouAEIOU":
            vwl.append(ch)
            count+=1
    print("\nReversed of the number only with the loop")
    for ch in range(len(x)):
        print(x[len(x)-ch-1],end="")       
    

    nlst = [12,3,2,45,3,43,5,7,32,5,7]
    max1 =nlst[0]
    min1=nlst[0]
    sum1=0
    for i in range(len(nlst)):
        for j in range(len(nlst)):
            if nlst[j]>max1 and nlst[j] > nlst[i]:
                max1 = nlst[j]

            if nlst[j]<min1 and nlst[j] < nlst[i]:
                min1 = nlst[j]
        sum1 = sum1+nlst[i]  
    print(f"\nmax. : {max1}")
    print(f"min. : {min1}\navg. : {sum1/len(nlst)}") 

    str1 = "There is a day after every night and you have to be strong on that night"
    print(str1.split(" "))
    wlst =[]
    cnt =0
    for x in str1.split(" "):
        if x[0] in "aeiouAEIOU":
            wlst.append(x)
         
    print(wlst, ": Vowels :", len(wlst))

practice()
wordAnalyzer()