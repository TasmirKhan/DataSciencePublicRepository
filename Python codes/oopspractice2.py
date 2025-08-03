print("This is a practice file for OOPs in Python")
class circle:
   
    def __init__(self, radius=2):
        self.radius = radius
        print("New circle created with radius:",radius)

    def area(self):
        print("Area of the circle is ", 3.14*self.radius*self.radius)
        return 3.14*self.radius*self.radius
    
    def perm(self):
        print("Perimeter of the circle is ", 2*3.14*self.radius)
        return 2*3.14*self.radius

c1 = circle(4)
# c1.area()
print(c1.area())
c1.perm()


print("\n\nNow we will create another class for practice")
class Employee:
    name = "Anonymous"
    age = "private"
    role = "Engineer"
    department ="Computer and AI"
    salary = "100000 "
    def __init__(self, role = "Anonymous", department ="Unknown", salary = 0):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)


e1 = Employee("Management", 230, "10 Millions")
e1.showdetails()

print("\n\nNow we will create another Engineer class for practice")
class Engineer(Employee):
    def __init__(self):
        print("Engineer class created")
        super().__init__()




e2 = Engineer()
e2.showdetails()

print("\n\nCreate a class named order which stores item and it's prices and Use dunder function __gt__() to convey that order of 1>order of 2 if the price of order 1 is greater than order 2")
class Order:
    def __init__(self, item = "unrecognised", price = "Not available"):
        self.item = item
        self.price = price
        print("New order created with item:", item ,"and price:", price)

    def __gt__(self, other):
        return self.price>other.price

o1 = Order("Pizza", 200)
o2 = Order("Burger", 150)
print(o1.item)
print(o2.item)

if o1>o2:
    print("Order 1 is greater than order 2")
else:
    print("Order 2 is greater than order 1")
    