print("In this program we will use finally block")
def func():
    try:
        a = int(input("Enter a Number:"))
        list = ['name', 'age', 'Qualification']
        print(list[a])
    except ValueError:
        print("Entered value is not an Integer")
    except IndexError:
        print("Index not found")
    except :
        print("Unknown Error found")
    finally:
        print("This is finally block and will always occur despite of the condition.")
    return 1234
x =func()
print("function return - ",x)