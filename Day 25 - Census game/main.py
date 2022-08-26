import pandas as pd
import turtle

path = "C:\PyLearning\projects\Day 25 - Census game"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = path + r"\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(path + "\states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    player_guess = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="").title()
    if player_guess == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        
        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv(path + "\states_to_learn.csv")
        break

    if player_guess in all_states:
        guessed_states.append(player_guess)
        state_data = data[data.state == player_guess]
        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(player_guess)

