#SUPER() METHOD  

# calls constructor of the base class

class Employee:
    def __init__(self):
        print("constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__() #calls the constructor of the base class
        print("constructor of manager")
    c=3

# o=Employee()
# print(o.a) 
# o=Programmer()
# print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)
