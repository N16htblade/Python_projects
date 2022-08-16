import random
import os
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print (logo)
print(f'Welcome to Hangman, word of the day is:')
display = ["_"] * word_length
print (' '.join(display))

lives = 6
end_of_game = False
guessed_letters = []

while not end_of_game:
    guess = input("Please guess a letter: ").lower()

    cls = lambda: os.system('cls')
    cls()

    for position in range(word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position]= letter
    
    if guess in guessed_letters:
        print("You have already tried this letter, try a different one.")
    elif guess not in chosen_word:
        lives -= 1
        print (f"Letter '{guess}' is not part of the word, please try again.")
    
    guessed_letters.append(guess)
    print (' '.join(display))

    if lives > 0:
        if "_" not in display:
            end_of_game = True
            print ("You Win!")
    else:
        end_of_game = True
        print ("You Lose.")
    
    print (stages[lives])