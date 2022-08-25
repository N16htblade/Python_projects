from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_START = [-225, -195, -165, -135, -105, -75, -45, -15, 15, 45, 75, 105, 135, 165, 195, 225]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            random_y = Y_START[random.randint(0, len(Y_START)-1)]
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
