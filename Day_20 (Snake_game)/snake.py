from turtle import Turtle, Screen
Constant_Speed = 20


class Snake:
    def __init__(self):
        self.segment = []
        self.snake_length()



    def snake_length(self):
        for i in range(0, 5):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=0 + (-20 * i), y=0)
            self.segment.append(new_snake)


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(Constant_Speed)

    def up_control(self):
        self.segment[0].setheading(90)

    def down_control(self):
        self.segment[0].setheading(270)

    def right_control(self):
        self.segment[0].setheading(0)

    def left_control(self):
        self.segment[0].setheading(180)

    def whole_control(self):
        screen = Screen()
        screen.listen()
        screen.onkey(self.up_control, "Up")
        screen.onkey(self.down_control, "Down")
        screen.onkey(self.right_control, "Right")
        screen.onkey(self.left_control, "Left")

