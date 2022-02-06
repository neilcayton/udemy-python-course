import turtle as t
import random
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_combination = (r, g, b)
    return color_combination


def draw_spirograph(size):
    for _ in range(360 // size):
        t.color(random_color())
        t.speed("fastest")
        t.circle(100)
        t.setheading(t.heading() + size)


draw_spirograph(2)
t.Screen().exitonclick()

