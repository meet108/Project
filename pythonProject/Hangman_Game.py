print("Welcome to Hangman Game!")
import random

lives = 6
words = ["apple", "beautiful", "Potato"]
chosen_word = random.choice(words)
print(chosen_word)

display = []
# for letter in range(len(chosen_word))

for letter in chosen_word:
    display += '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lost !")
    if '_' not in display:
        game_over = True
        print("You won !")
