import random
'''
if you choose rock and computer choose scissors you win or
if you choose scissors and computer choose paper you win or
if you choose paper and computer choose rock you win otherwise you will lose 



'''

choices=["rock","paper","scissors"]
while True:

    your_choice=input("Enter you choice :rock,paper,scissors of exit to end the game: ").lower()

    if your_choice=="exit":
      print("Thanks for playing!")
      break
    
    if your_choice not in choices:
      print("invalid choice try again")
      continue
    

    computer_choice=random.choice(choices)
    print(f"your choice is :{your_choice}\n computer choice is {computer_choice}")
    if your_choice==computer_choice:
      print("Its a tie")
    elif your_choice=="rock" and computer_choice=="scissors":
      print("You win!")
    elif your_choice=="scissors" and computer_choice=="paper":
       print("You win")
    elif your_choice=="paper" and computer_choice=="rock":
      print("you win")
    else:
      print("You lose")
