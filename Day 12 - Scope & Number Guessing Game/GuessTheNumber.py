from art import logo
from replit import clear
import random


def game():
    play_again = "y"
    while play_again == "y":
        clear()
        print(logo)
        print("Welcome to the Number Guessing Game !!")

        print("I'm thinking of a umber between 1 and 100.")
        my_number = random.randint(1,100)
        print(f"My number is {my_number}")
        lives = {
            "hard":5,
            "easy": 10,}

        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        no_of_lives = lives[difficulty_level]

        for _ in range(no_of_lives):
            print(f"You have {no_of_lives - _} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == my_number:
                print(f"You got it! The answer was {my_number}")
                break
            elif guess > my_number:
                print("Too high.\nGuess again.")
            elif guess < my_number:
                print("Too low.\nGuess again.")

        play_again = input("Do you want to play again, press 'y' to continue and 'n' to exit: ").lower()
        if play_again == "n":
            break

want_to_play = input("Do you want to play a number guessing game ? Press 'y' to play or any key to exit: ")

if want_to_play == "y":
    game()