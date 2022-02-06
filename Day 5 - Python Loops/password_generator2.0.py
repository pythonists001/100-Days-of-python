#Password Generator Project
from replit import clear
from art import key, logo
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
  generate_password = True

  while generate_password:
    clear()
    print(logo)
    print(key)
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password = ""

    for _ in range(1, nr_letters + 1):
      # 1 -4
      # random_char = random.choice(letters)
      # password += random_char
      password += random.choice(letters)

    for _ in range(1, nr_symbols + 1):
      password += random.choice(symbols)

    for _ in range(1, nr_numbers + 1):
      password += random.choice(numbers)  

    strong_password = ''.join(random.sample(password,len(password)))
    print(strong_password)
    choice = input("Do you want to generate a new password. Press 'y' to continue or any key to exit ").lower()
    if choice == "y":
      password_generator()
    else:
      generate_password = False
      break

need_password = input("Do you want to generate a strong password. press 'y' to continue or any key to exit ").lower()
if need_password == "y":
  password_generator()