from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1400, height=900)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((650, 0))
l_paddle = Paddle((-650, 0))
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 420 or ball.ycor() < -420:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 615 or ball.distance(l_paddle) < 50 and ball.xcor() < -615:
        ball.bounce_x()

    # Detect if the ball goes beyond r_paddle
    if ball.xcor() > 680:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if the ball goes beyond l_paddle
    if ball.xcor() < -680:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
