import random
'''
1 for snake 
-1 for water
0 for gun
'''
youDict={"snake": 1,"water": -1,"gun": 0}
reverseDict={1:"snake",-1:"water",0:"gun"}
youstr = input("Enter your choice snake ,water or gun: ")
    

computer =random.choice([-1,0,1])
you = youDict[youstr]
print(f"Your choice is {reverseDict[you]} \n computer choice is {reverseDict[computer]}\n")
if(computer==you):
    print("Its a draw")

else:        
  

        if(computer ==-1 and you ==1):
            print("you win!")
        elif(computer ==-1 and you ==0):
             print("You lose!")
        elif(computer ==1 and you ==-1):
            print("you win!")
        elif(computer ==1 and you ==0):
            print("You lose!")
        elif(computer ==0 and you ==1):
            print("you lose!")
        elif(computer ==0 and you ==-1):
            print("You win!")

        else:
            print("something went wrong:")


   



     

    

