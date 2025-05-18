# class employee:
#     company="ITC"
#     name="Harsh"
#     def show(self):
#         print(f"The name of the employee is{self.name}and the salary is {self.company}")

# class coder:
#     language="python"
#     def printLanguage(self):
#         print(f"Out of all language here is your language:{self.language}")



#multiple inheritance
# class programmer(employee,coder):
#     company="ITC infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.company} language")

# a=employee()
# b=programmer()
 
# b.show()
# b.printLanguage()
# b.showLanguage()

# print(a.company,b.company)


#multi-level inheritance
class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

o=Employee()
print(o.a) #print the attribute
# print(o.b) shows an error as there is no b attribute in employee class
o=Programmer()
print(o.a,o.b)

o=Manager()
print(o.a,o.b,o.c)