import random

choices = ['rock', 'paper', 'scissors']
User_score = 0
computer_score = 0

def game(user, computer):
 global User_score
 global computer_score
 print(f" You chose {user}, computer chose {computer}.")
 if user == computer:
  print(f"Both players selected {user}. It's a tie!\n")
 elif user == "rock":
  if computer == "scissors":
   User_score += 1 
   print(f" Rock smashes scissors! You scored 1 point. Your score is {User_score}, computer score is {computer_score}\n")
  else:
   computer_score += 1
   print(f"Paper covers rock! Computer scored 1 point. Your score is {User_score}, computer score is {computer_score}\n ")


 elif user == "paper":
  if computer == "rock":
   User_score+= 1
   print(f"Paper covers rock! You scored 1 point. Your score is {User_score}, computer score is {computer_score}\n ")
  else:
   computer_score += 1
   print(f" Scissors cuts paper! Computer scored 1 point. Your score is {User_score}, computer score is {computer_score}\n ")

 elif user == "scissors":
  if computer == "paper":
   User_score+= 1
   print(f" Scissors cuts paper! You scored 1 point. Your score is {User_score}, computer score is {computer_score}\n ")
  else:
   computer_score += 1
   print(f" Rock smashes scissors! Computer scored 1 point. Your score is {User_score}, computer score is {computer_score}\n")

while True:
 if User_score == 10:
  print("="*30, "\n Your score reached 10. YOU WIN!\n", "="*30)
  exit()
 elif computer_score == 10:
  print("="*30, "\n Computer score reached 10. COMPUTER WIN!\n", "="*30)
  exit()
  
 user_choice = input("Enter a choice ( rock, paper, scissor): ") .lower()
 computer_choice = random.choice(choices)

 if user_choice == "quitgame":
  print("FINISH")
  exit()
 elif not user_choice in choices:
  print("YOU CHOSE A WRONG CHOSE, PLEASE TRY AGAIN.")
 else:
  game(user_choice, computer_choice)