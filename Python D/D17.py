print("Loops in python")

def multTable():
    x = int(input("Enter the number:"))
    for a in range(1,11):
        print(f"{a} x {x} = {a*x}")

def rangeMultTable():
    x,y = int(input("Enter the range from to :")), int(input())
    count =1
    while(x<=y):
        while(count<=10):
            print(f"{x*count}",end=" ")
            count+=1
        count =1
        x +=1
        print()

multTable()
rangeMultTable()