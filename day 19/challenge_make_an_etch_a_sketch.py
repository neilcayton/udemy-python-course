
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    return tim.forward(10)


def move_backward():
    return tim.back(10)


def move_left():
    return tim.left(10)


def move_right():
    return tim.right(10)


def clear():
    return tim.goto(0, 0), tim.clear()


def controls():
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="d", fun=move_right)
    screen.onkey(key="a", fun=move_left)
    screen.onkey(key="c", fun=clear)


controls()
screen.listen()
screen.exitonclick()