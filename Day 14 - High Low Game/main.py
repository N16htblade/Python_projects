from art import logo, vs
from game_data import data
import random
import os

def check_entry(entry, pickA, pickB):
    followersA = int(pickA['follower_count'])
    followersB = int(pickB['follower_count'])
    if followersA > followersB and entry == 'A':
        return pickB
    elif followersA < followersB and entry == 'B':
        return pickB
    else:
        return

def cleanup():
    cls = lambda: os.system('cls')
    cls()
    print (logo)

def play_game (pickA, final_score):
    for i in range(len(data)-1):
        if data[i]['name'] == pickA['name']:
            del data[i]
    pickB = random.choice(data)

    print (f"Compare A: {pickA['name']}, a {pickA['description']}, from {pickA['country']}.")
    print (vs)
    print (f"Compare B: {pickB['name']}, a {pickB['description']}, from {pickB['country']}.")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")
    result = check_entry(user_choice, pickA, pickB)
    cleanup()

    if result == pickA or result == pickB:
        final_score += 1
        print (f"You're right! Current score: {final_score}")
        play_game(result, final_score)
    else: 
        print (f"Sorry, that's wrong. Final score = {final_score}")


while input("\nWould you like to play the guessing game? y/n: ") == 'y':
    cleanup()
    random_pickA = random.choice(data)
    play_game(random_pickA, 0)