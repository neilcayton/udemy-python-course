from random import Random
from turtle import Turtle


class Food:
    def __init__(self):
        self.snake_food = Turtle()
        self.snake_food.penup()
        self.snake_food.shape("circle")
        self.snake_food.color("blue")
        # self.snake_food.turtlesize(1)

    def generate_loc(self):
        random_gen = Random()
        food_x_cor = random_gen.randint(-500, 500)
        food_y_cor = random_gen.randint(-500, 500)
        self.snake_food.goto(food_x_cor, food_y_cor)

    def eating_rule(self, segment):
        segment_pos_x = int(segment[0].pos()[0])
        segment_pos_y = int(segment[0].pos()[1])

        food_x , food_y = int(self.snake_food.xcor()), int(self.snake_food.ycor())
        print(food_x)
        if self.snake_food.pos() == None:
            new_foood = self.generate_loc()
