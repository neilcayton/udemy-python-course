from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Level:  {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreBoard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("____ GAME OVER ____", align="center", font=FONT)

