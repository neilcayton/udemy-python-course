from turtle import Screen,Turtle
from paddle import Paddle
import time

screen = Screen()

screen.setup(800, 800)
screen.title("Ping-pong Game")
screen.bgcolor("black")
time.sleep(0.1)
paddle_class = Paddle()
screen.exitonclick()
