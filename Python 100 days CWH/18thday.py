print("In this program we are going to learn about the use of while loops")

x = int(input("Enter Your password "))
count = 0
while(count<3):
    print("Enter your password :")
    temp = int(input())
    if(temp == x):
        print("Password Matched \t You are Good to go")
        break
    else:
        count = count+1
if(count==3):
    print("Try Limit reached")