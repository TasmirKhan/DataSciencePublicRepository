import random as rd


def game(x):
    s = rd.randint(1,x)
    i=1
    while(i<=7):
        inpt = int(input(f"Attempts left {8-i} :"))
        if(inpt == s):
            print("You win")
            break
        elif(inpt < s):
            print("too low")
            i+=1
        elif(inpt > s):
            print("too high")
            i+=1
        if(i==8):
            print(f"Game over, Secret no. is {s}")
            break




print("Number guessing game:-")
print("Enter the level which you want to play \n1 for easy\n2 for Medium\n3 for Hard")
x = int(input())
if(x==1):
    game(150)
elif(x==2):
    game(300)
elif(x==3):
    game(500)
else:
    print("Invalid input!")
