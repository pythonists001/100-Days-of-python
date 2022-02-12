import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
# print(f"chosen word: {chosen_word}")
end_of_game = False
lives = 6
display = []

os.system("cls")
print(logo)

for _ in chosen_word:
    display += "_"

print(f"{' '.join(display)}\n\n and is {word_length} letters long.")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls")

    if guess in display:
        print(f"{guess} already guessed.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The word is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
