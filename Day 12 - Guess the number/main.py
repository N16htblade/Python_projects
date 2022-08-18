from distutils.command import check
from art import logo
import os
import random

def check_guess (player_guess, random_number):
    if player_guess > random_number:
        return "high"
    elif player_guess < random_number:
        return "low"
    else:
        return

def play_game():
    print (logo)
    print ("Welcome to the Number Guessing Game!")
    print ("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a dificuly. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        player_life = 10
        print("You start with 10 attempts.")
    else:
        player_life = 5
        print("You start with only 5 attempts.")

    random_number = random.randint(1, 100)
    stop_game = False

    while player_life > 0 and not stop_game:
        guess = int(input("Make a guess: "))
        if check_guess(guess, random_number) == "high":
            player_life -=1
            print (f"""        
            Too high.
            Guess again.
            You have {player_life} attempts remaining to guess the number.
            """)
        elif check_guess(guess, random_number) == "low":
            player_life -=1
            print (f"""        
            Too low.
            Guess again.
            You have {player_life} attempts remaining to guess the number.
            """)
        else:
            stop_game = True
            print ("You guessed the number!")
    
    if player_life == 0:
        stop_game = True
        print (f"Sorry, but you have run out of attempts.")

   
while input("\nWould you like to play the Guessing Game? y/n: ") == "y":
    cls = lambda: os.system('cls')
    cls()
    play_game()