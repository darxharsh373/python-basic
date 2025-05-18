'''Create a class “Programmer” for storing information of few programmers 
 working at Microsoft. '''

class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):

        self.name=name
        self.salary=salary
        self.pin=pin

p=programmer("Harsh",1200000,853202)
print(p.salary,p.name,p.pin,p.company)
r=programmer("Aniket",1200000,853202)
print(r.salary,r.name,r.pin,r.company)