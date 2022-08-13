print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print ("Welcome to Treasure Island.")
print ("Your mission is to find the treasure.")

leftRight = input("You set foot on the local docks and you take in view of the local village and sureal jungle going up the mountains behind. Do you go left or right?\n").lower()
if leftRight == "left":
    waitSwim = input("You make your way into the dense jungle to find yourself in front of a river. Would you like to wait or swim?\n").lower()
    if waitSwim == "wait":
        doorColor = input("It's your lucky day, a local villager just happens to come down the river with a boat and helps you accross the river.\nAfter several more hours of walking, you find yourself in a cave, in front of a strange set of doors.\nOne is Red, one is Yellow and the last one is Blue. Which one would you like to go thru?\n").lower()
        if doorColor == "yellow":
            print ("Congratulations, you have found the tresure!")
        elif doorColor == "red":
            print ("This door was holding back a pack of hungry Wolfs.\nGame Over.")
        elif doorColor =="blue":
            print ("This door leads to a Extended Warranty Agent. Game Over.")
        else:
            print ("You thought about it for too long and starved.\nGame Over.")
    else:
        print ("You go into the water but forget you can't swim.\nGame Over.")
else:
    print ("You didn't realize you were at the end of the dock and fell into shark infested water!\nGame Over.")


