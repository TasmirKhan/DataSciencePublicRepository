print("Today we are going to see the match case in python")
x = int(input("Enter your no. : "))
match x:
    case 1:
        print("Entered no. is 1")
    case 2:
        print("Entered no. is 2")
    case _ if x!=3:
        print("Entered no. is not 3")
    case _ if(x!=-1):
        print("Entered no. is not -1")
    case _:
        print("Entered no. is Unique identity")

