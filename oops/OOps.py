class employee:
    # name="Harsh"
    language="Py"
    salary=1200000
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creatng an object")   #dunder method which is automatically called
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    # def greet(self):
    #     print("Good morning")

    @staticmethod
    def greet():
        print("Good morning")

harsh=employee("Harsh",120000,"Javascript")
# harsh.language="Javascript"
print(harsh.name,harsh.salary,harsh.language)

# aniket=employee()
# print(aniket.salary,aniket.language)

# harsh.greet()
# harsh.getInfo()
