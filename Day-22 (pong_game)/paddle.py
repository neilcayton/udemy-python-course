from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.speed(100)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=9)
        self.color("white")
        self.goto(x=pos, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def all_command(self):
        self.go_up()
        self.go_down()