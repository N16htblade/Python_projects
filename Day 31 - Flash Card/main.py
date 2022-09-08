from email.mime import image
from tkinter import *
from turtle import color
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#-------------------------- FUNCTIONALITY --------------------#
try:
    data = pandas.read_csv(R"C:\PyLearning\projects\Day 31 - Flash Card\data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(R"C:\PyLearning\projects\Day 31 - Flash Card\data\french_words.csv")

words_dic = data.to_dict(orient="records")
random_pair = {}

def reset_card():
    global random_pair, flip_timer
    window.after_cancel(flip_timer)
    random_pair = random.choice(words_dic)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_pair["French"], fill="black")
    flip_timer = window.after(3000, flip_card)

def clear_card():
    words_dic.remove(random_pair)
    data = pandas.DataFrame(words_dic)
    data.to_csv("C:\PyLearning\projects\Day 31 - Flash Card\data\words_to_learn.csv", index=False)
    reset_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_pair["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)

#-------------------------- USER INTERFACE -------------------#
#Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

#Canvas
canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file="C:\PyLearning\projects\Day 31 - Flash Card\images\card_back.png")
card_front_image = PhotoImage(file="C:\PyLearning\projects\Day 31 - Flash Card\images\card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#Buttons
correct_button_image = PhotoImage(file=R"C:\PyLearning\projects\Day 31 - Flash Card\images\right.png")
correct_button = Button(image=correct_button_image, borderwidth=0, command=clear_card)
correct_button.grid(column=0, row=1)

wrong_button_image = PhotoImage(file="C:\PyLearning\projects\Day 31 - Flash Card\images\wrong.png")
wrong_button = Button(image=wrong_button_image, borderwidth=0, command=reset_card)
wrong_button.grid(column=1, row=1)

reset_card()
window.mainloop()