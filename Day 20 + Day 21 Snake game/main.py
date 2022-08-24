from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

score = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        score =+ 1
        score_board.increase_score()
        snake.extend()

    # Detect collision with wall:
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()

    # Detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()