import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.generate_loc()

    def generate_loc(self):
        food_x_cor = random.randint(-250, 250)
        food_y_cor = random.randint(-250, 250)
        self.goto(food_x_cor, food_y_cor)


