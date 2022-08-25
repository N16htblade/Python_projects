from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 30, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 250)
        self.write(f"{self.p1_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(150, 250)
        self.write(f"{self.p2_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.goto(0, 0)
        self.write(f"{player} HAS WON!", align=ALIGNMENT, font=FONT)

    def p1_point (self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point (self):
        self.p2_score += 1
        self.update_scoreboard()