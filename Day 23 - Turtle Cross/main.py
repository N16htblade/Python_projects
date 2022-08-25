import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtly")
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # Check if player made it to the end
    if player.ycor() >= 280:
        scoreboard.points()
        player.reset()
    
    # Check if player hit a car
    for each_car in car.cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()