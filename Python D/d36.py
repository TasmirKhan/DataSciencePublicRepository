
from abc import ABC,abstractmethod
class shape():
    @abstractmethod
    def method(self):
        pass
    
class circle(shape):
    def method(self):
        print("Circular shape")
        
class triangle(shape):
    def method(self):
        print("Traingular shape")
        
c1 = circle()
c1.method()

t1 = triangle()
t1.method()


class car():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"This is a {self.name} car"
    

    def __eq__(self,other):
        return self.name == other.name
    
c1 = car("bmw")

c2 = car("mercedes")
print(c1,"\n",c2)
print(c1==c2)

print("Overload + operator.")
class vector():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
        pass
    def __add__(self,other):
        return (self.n1+other.n1,self.n2+other.n2) 

v1 = vector(2,3)
v2 = vector(4,5)

v3 = v1+v2
print(v3)

