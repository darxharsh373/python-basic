'''Write a class “Calculator” capable of finding square, cube and square root of a 
number'''
class calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square is {self.n*1/2}")
   
    @staticmethod # q_4 Add a static method in problem 2, to greet the user with hello. 
    def greet():
        print("Hello there:")
x=int(input("Enter a number to find its cube ,square and squareroot "))

a=calculator(x)
a.greet()
a.square()
a.cube()
a.squareroot()