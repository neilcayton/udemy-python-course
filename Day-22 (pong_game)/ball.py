from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(20)
        self.color("white")
        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.showturtle()
        self.ycor_move = 10
        self.xcor_move = 10

    def move(self):
        new_xcor = self.xcor() + self.xcor_move
        new_ycor = self.ycor() + self.ycor_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.ycor_move *= -1

    def bounce_x(self):
        self.xcor_move *= -1

    def reset_position(self):
        self.goto(0, 0)