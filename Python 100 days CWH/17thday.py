print("In this python program we are going to see the use of for loops")

# name = "TasmirKhan"
# for i in name:
#     print(i)
#     if(i=="r"):
#         print("This is Surname starting")

colors = ["Red", "Blue", "Green", "Yellow"]
for color in colors:
    print(color)
    if(color == "Green"):
        print("This is Green color")
        for i in color :
            print(i)


print("Printing no. from default value(0) to 7(upper range)")
for k in range(7):
    print(k)
    print(k+1, "This is",k,"+1")

print("Pringting no. from 10 to 15")
for k in range(10, 15):
    print(k)

print("Printing no. from 20 with a jump of 7 every time till 100")
for k in range(20, 100, 7):
    print(k)
    