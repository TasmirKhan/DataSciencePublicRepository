print("File Handling")

f = open("example.txt",'w')
f.write("Hello,Python!")
f.close()

f = open("example.txt","a")
f.write(" we can append through this section !")
f.close()

# f = open("example3.txt", "x") already exists therefore showing error
f.close()

f = open("example.txt","r")
content = f.read()
f.close()
print(content)

f = open("example.txt","r")
for line in f:
    print(line.strip())
f.close()

print("Practice section==>")

f = open("notes.txt","w")
f.write("This is line 1.\nThis is line 2.\nThis is line 3.\n")
f.close()

f = open("notes.txt","r")
for line in f:
    print(line.strip())
f.close()

f = open("notes.txt", "a")
f.write("\nThis is the appended 4th line of notes.")
count =0
f = open("notes.txt","r")
print("After appending in the new file: ")
for line in f:
    print(line.strip())
    count+=1
print("Total number of lines is ", count)
f.close()

count =0
with open("notes.txt", "a") as f:
    f.write("\nThis is the final appended line of this text file.")
    f.close

f  = open("notes.txt", "r")
for line in f:
     count+=1
print("The total number of lines in this file is: ",count)


print("EXTRA TASK:-\nBuild personal notes app")

class personal_notes_app:
    def __init__(self):
        print("Enter:\n0 -> create a new file\n1 -> write a file\n2 -> view a file\n3 -> append a file\n4 -> exit")
    
    def create(self):
        y = input("Enter the file name to be created along with the extentsion: ")
        try:
            f = open(y,"x")
            f.close()
            print(f"file {y} is created")
        except(FileExistsError):
            print("File already exists!")
            return

    def write(self):
        f1 = input("Enter the name of the file to be write in: ")
        try:
            with open (f1,"w") as f:
                text = input("write your content\n")
                f.write(text)
        except(FileNotFoundError):
            print("File doesn't Exist!")
            return
            
        print("task completed")

    def view(self):
       f1 = input("enter the name of the file")
       try:
            with open (f1,"r") as f:
               print(f.read())
               print("[Line by line]")
               for line in f:
                   print(line.strip())
       except(FileNotFoundError):
           print("File doesn't Exist!")
           return 
           

   
    def append(self):
        f1 = input("Enter the name of the file to be write in: ")
        try:
            with open (f1,"a") as f:
                text = input("write your content\n")
                f.write(text)
        except(FileNotFoundError):
            print("File doesn't exist!\nFirst create it")
            return 
        print("task completed ")

    def run(self):
        while(True):
           try:
               x = int(input())
           except(ValueError):
               print("Not an integer")
               continue
            
           match x:
                case 0:
                    self.create()
                case 1:
                    self.write()
                case 2:
                    self.view()
                case 3:
                    self.append()
                case 4:
                    print("Exiting......")
                    break
                case _:
                    print("Invalid input! Try again...")
        

notes1 = personal_notes_app()
notes1.run()