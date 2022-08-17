from turtle import Turtle


class Paddle():
    def __init__(self):
        self.paddle = []
        self.paddle_part = 4
        self.paddle_length()


    def create_paddle(self, addlen):

        paddle1 = Turtle()
        paddle1.speed(100)
        paddle1.penup()
        paddle1.shape("square")
        paddle1.shapesize(2)
        paddle1.color("white")
        paddle1.goto(x=350, y= 0 + (-20 *addlen))
        self.paddle.append(paddle1)

    def paddle_length(self):
        for i in range(0, self.paddle_part):
            self.create_paddle(i)


    # def vertical_upanddown(self):
