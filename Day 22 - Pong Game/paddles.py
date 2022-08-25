from turtle import Turtle
STARTING_POSITION=[(350,0), (-350,0)]
MOVE_DISTANCE = 20


class Paddles(Turtle):

    def __init__(self, coordonates):
        super().__init__()
        self.shape ("square")
        self.shapesize(stretch_wid=1 ,stretch_len=5, outline=None)
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(coordonates)

    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def down(self):
        self.backward(MOVE_DISTANCE)
