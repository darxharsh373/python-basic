# Use comparison operator to find out whether ‘a’ given variable a is greater than 
# ‘b’ or not. Take a = 34 and b = 80 

a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))
if(a<b):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")