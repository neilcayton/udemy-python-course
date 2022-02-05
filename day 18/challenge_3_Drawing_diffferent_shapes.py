import random
import turtle as t

colors = ["red", "yellow", "blue", "green", "violet", "orange", "medium spring green","midnight blue"]


def angle(number_sides):
    side_angle = 360 / number_sides
    return side_angle


move = 3
while move != 11:
    t.speed(1)
    t.width(10)
    for i in range(move):
        t.color(random.choice(colors))
        t.right(angle(move))
        t.forward(100)
    move += 1

t.Screen().exitonclick()
