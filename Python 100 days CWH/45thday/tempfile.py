def welcome():
    print("Hello Peter!")
def confidential():
    print("This is the confidential and only can be run with the main file")

if __name__ == "__main__":
    print("This is printed Directly.")
    welcome()
    confidential()
     
if __name__ == "tempfile":
    print("This is printed Indirectly by temprory file.")
    welcome()