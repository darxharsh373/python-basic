# def checkStatus(self, a, b, flag):
#        if(a>0 or (b>0 and flag is False)):
#            return True;
#        elif(a<0 and b<0 and flag is True):
#             return True;
#        else:
#             return False;
          
# def checkOddEven(x):
    
#     if x % 2 ==0:
#         # print("Even")
#         return "Even"
      

#     else:
#         # print("Odd")
#         return "Odd"
    
# checkOddEven(1)
def fizzBuzz(number):
    if number %3 == 0 and number%5 == 0:
        print( "FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print( "Buzz")
    else:
        print (number)
    
fizzBuzz(15)