print("Program to show file input output")
with open("practice.txt", "w+") as f:
    f.write("Hi everyone \nWe are learning file I/O \nUsing Java.\nI like programming in java")
    
# with open("practice.txt", "r") as f2:
#     print(f2.read())
#     f2.seek(0)
#     print(f2.read(5))
#     f2.seek(0)
#     print(f2.readline())
#     f2.seek(0)
#     print(f2.readlines())
    
with open("practice.txt", "r") as f:
    content = f.read()
    print(content)
    print(content.split())
    content = content.replace("java","Python").replace("Java", "Python")
    print(content)
    if "learning" in content:
        print("Yes")
    else:
        print("No")

