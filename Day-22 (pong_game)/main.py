from turtle import Screen
from paddle import Paddle
from ball import Ball

import time

screen = Screen()

screen.setup(800, 800)
screen.title("Ping-pong Game")
screen.bgcolor("black")

screen.tracer(0)

paddle_l = Paddle(pos=350)
paddle_r = Paddle(pos=-350)
ball = Ball()
line = Paddle.line

screen.listen()
screen.onkeypress(paddle_r.go_up, "w")
screen.onkeypress(paddle_r.go_down, "s")
screen.onkeypress(paddle_l.go_up, "Up")
screen.onkeypress(paddle_l.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()
    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.bounce_y()
    # game_is_on = False
    if paddle_l.distance(ball) < 50 and ball.xcor() > 340\
            or paddle_r.distance(ball) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()
