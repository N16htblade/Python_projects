from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

file_path = "c:\PyLearning\projects\Day 20 + Day 21 Snake game\high_score.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file_path, mode="r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        high_score = str(self.high_score)
        with open(file_path, mode="w") as file:
            file.write(high_score)
    
    def increase_score (self):
        self.score += 1
        self.update_scoreboard()
        