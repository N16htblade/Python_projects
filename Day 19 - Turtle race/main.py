import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

def create_turtle(color):
    t = Turtle("turtle")
    t.color(color)
    t.penup()
    return t

for color in colors:
    our_turtle = create_turtle(color)
    no_of_turtle = colors.index(color)
    x = -230
    y = 50 * (no_of_turtle - 3) + 25
    our_turtle.setpos(x, y)
    all_turtles.append(our_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        x = round(turtle.xcor(), 1)
        if x >= 230:
            race_on = False
            winer = turtle.color()[0]
            if user_choice == winer:
                print (f"You win, {user_choice} won!")
            else:
                print (f"You lost, {winer} won.")
            break

screen.exitonclick()