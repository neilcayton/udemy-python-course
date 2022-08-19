from turtle import Screen
from paddle import Paddle
# import time

screen = Screen()

screen.setup(800, 800)
screen.title("Ping-pong Game")
screen.bgcolor("black")
# time.sleep(0.1)
screen.tracer(0)

paddle_l = Paddle(pos=350)
paddle_r = Paddle(pos=-350)

game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkeypress(paddle_r.go_up, "w")
    screen.onkeypress(paddle_r.go_down, "s")
    screen.onkeypress(paddle_l.go_up, "Up")
    screen.onkeypress(paddle_l.go_down, "Down")
screen.exitonclick()
