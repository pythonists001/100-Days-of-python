rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import os
import random
num = "0"
user_choice = ""
computer_choice = ""

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def choice(num):
  if num == "0":
    print(rock)
  elif num == "1":
    print(paper)
  elif num == "2":
    print(scissors)
  else:
    print("Wrong choice")

def printWLD(result):
  if result == "win":
    print("Nevaan won")
  elif result =="lose":
    print("Nevaan lose")
  else:
    print("It's a draw")

## 0 rock
## 1 paper
## 2 scissors

def win_rules(user_choice,computer_choice):
  if user_choice == "0" and computer_choice == "0":
    printWLD("draw")
  elif user_choice == "0" and computer_choice == "1":
    printWLD("lose")
  elif user_choice == "0" and computer_choice == "2":
    printWLD("win")
  elif user_choice == "1" and computer_choice == "0":
    printWLD("win")
  elif user_choice == "1" and computer_choice == "1":
    printWLD("draw")
  elif user_choice == "1" and computer_choice == "2":
    printWLD("lose")
  elif user_choice == "2" and computer_choice == "0":  
    printWLD("lose")
  elif user_choice == "2" and computer_choice == "1":
    printWLD("win")
  elif user_choice == "2" and computer_choice == "2":
    printWLD("draw")

def game_logic(user_choice,computer_choice):
  choice(user_choice)
  print("Papa chose:")
  choice(computer_choice)
  win_rules(user_choice,computer_choice)

clearConsole()
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Press N key to end the game.")

while user_choice in ["0","1","2"]:   
  computer_choice = str(random.randint(0,2))
  game_logic(user_choice,computer_choice)
  user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Press N key to end the game.")

print("Game Over!!") 




