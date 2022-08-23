import turtle as t
import random

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
t.screensize(canvwidth=850, canvheight=850, bg=None)
t.setup(width=900, height=900)
t.colormode(255)
tim.pensize(20)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(420)
tim.setheading(0)

def draw_points():
    for number in range (10):
        tim.color(random.choice(color_list))
        tim.pendown()
        tim.forward(0)
        tim.penup()
        if number < 9:
            tim.forward(70)

def next_row():
    tim.left(90)
    tim.forward(70)
    tim.right(90)
    tim.backward(630)

for number in range (10):
    draw_points()
    if number < 9:
        next_row()

t.exitonclick()