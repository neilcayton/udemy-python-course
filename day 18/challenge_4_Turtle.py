import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_combination = (r, g, b)
    return color_combination


def random_angles():
    angle = [45, 135, 225, 315]
    # angle = [90, 180, 270, 0]
    # angle = [30, 150, 240, 330]
    angles = random.choice(angle)
    return angles


while True:
    t.width(20)
    t.color(random_color())
    t.forward(20)
    t.speed("fastest")
    t.setheading(random_angles())

