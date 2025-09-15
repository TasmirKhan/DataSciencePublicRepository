print("Grading System Program")

def ifGradingelse():
    x = int(input("Enter the marks: "))
    if(x==100):
        print("Perfect Score")
    if(x>=90 and x<100):
        print("Grade A")
    elif(x>=75 and x<=89):
        print("Grade B")
    elif(x>=50 and x<=74):
        print("Grade C")
    elif(x<50):
        print("Fail")
    else:
        print("Invalid input!")

def matchGradingcase():
    y = int(input("Enter the marks: "))
    match y:
        case _ if 100>y>=90:
            print("Grade A")
        case _ if 89>=y>=75:
            print("Grade B")
        case _ if 74>=y>=50:
            print("Grade C")
        case _ if y<50:
            print("Fail")
        case _:
            print("Invalid input")

ifGradingelse()
matchGradingcase()