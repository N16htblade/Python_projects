from turtle import Screen
from paddles import Paddles
from ball import Ball
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


player1 = Paddles((-350, 0))
player2 = Paddles((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

player1_score = 0
player2_score = 0

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("wall")
    
    # Detect collision with paddle:
    if ball.distance(player1) < 50 and ball.xcor() < -330 or ball.distance(player2) < 50 and ball.xcor() > 330:
        ball.bounce("paddle")
    
    # Detect if right paddle missed ball
    if ball.xcor() > 380:
        player1_score += 1
        scoreboard.p1_point()
        ball.reset_ball()
    
    # Detect if left paddle missed ball
    if ball.xcor() < -380:
        player2_score += 1
        scoreboard.p2_point()
        ball.reset_ball()

    # End game if someone reaches 3 wins
    if player1_score == 3:
        scoreboard.game_over("PLAYER 1")
        game_is_on = False
    elif player2_score == 3:
        scoreboard.game_over("PLAYER 2")
        game_is_on = False

        #score_board.increase_score()



screen.exitonclick()


