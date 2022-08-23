from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()

screen.setup(800, 800)
screen.title("Ping-pong Game")
screen.bgcolor("black")

screen.tracer(0)
scoreboard = Scoreboard()
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
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # print(ball.xcor())
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    # game_is_on = False
    if paddle_l.distance(ball) < 50 and ball.xcor() > 330 \
            or paddle_r.distance(ball) < 50 and ball.xcor() < -330:

        print("made contact")
        ball.bounce_x()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        ball.reset_speed()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
        ball.reset_speed()
screen.exitonclick()
