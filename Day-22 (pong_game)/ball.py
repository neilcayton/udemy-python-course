from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=2)
        self.penup()
