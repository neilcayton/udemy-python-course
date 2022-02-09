from turtle import Turtle, Screen
from random import random


t = Turtle()
r = random()
screen = Screen()
screen.setup(500, 400)
screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter Color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(len(colors)):
    colors[i] = Turtle()
    t.shape("turtle")
    my_color = colors[i]
    t.color(f"{my_color}")
    t.goto(x=-220, y=-100 + 10 * i)
    screen.exitonclick()
#
