import random
from replit import clear
from art import logo,vs
from game_data import data

def get_random_account():
    return random.choice(data)

def getDetails(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}"

#print(getDetails(get_random_account()))

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play():
    score = 0

    game_should_continue = True

    while game_should_continue:
        clear()
        print(logo)
        print(f"Your current score : {score}")
        account_a = get_random_account()
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']

        print(f"Comapre A: {getDetails(account_a)}")
        print(vs)
        print(f"Comapre B: {getDetails(account_b)}")
        choice = input("Your Answer. Press 'a' or 'b': ").lower()
        if check_answer(choice,a_followers,b_followers):
            score += 1
            print(f"Your score : {score}")
        else:
            print(f"Your Score : {score}")
            game_should_continue = False
            print("Game Over")

    play_again = input("Do you want to play again. Press 'y' to continue and 'n' to exit ").lower()
    if play_again == "y":
        play()

play()