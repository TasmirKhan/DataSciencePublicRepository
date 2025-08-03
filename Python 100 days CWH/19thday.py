print("Here we are going to make a program using break and continue")
i =0
while(True):
    i = i+1
    if(i%2==0):
        continue
    print(i)
    if(i%5==0):
        print("Reached the limit")
        break

