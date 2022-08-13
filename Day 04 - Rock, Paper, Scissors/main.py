import random

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

game = [rock, paper, scissors]

playerNumber = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if playerNumber < 0 or playerNumber > 2:
    print ("You have typed an invalid number.")
    quit()

playerChoice = game[playerNumber]
print (playerChoice)

computerNumber = random.randint(0,2)
computerChoice = game[computerNumber]
print (f"Computer chose: {computerChoice}")

if playerNumber == 0 and computerNumber == 2:
    print ("You Won!")
elif playerNumber == 1 and computerNumber == 0:
    print ("You Won!")
elif playerNumber == 2 and computerNumber == 1:
    print ("You Won!")
elif playerNumber == computerNumber:
    print ("It's a Draw.")
else:
    print ("You Lost.")
