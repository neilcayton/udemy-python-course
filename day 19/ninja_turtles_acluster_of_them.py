from turtle import Turtle, Screen
import random

is_race_on = False
t = Turtle()

screen = Screen()
screen.setup(700, 570)
screen.bgpic("Capture.PNG")
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter Color: ")

colors = ["red", "cyan", "pink", "yellow", "green", "blue", "purple"]
all_turtles = []
for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=-120 + 40 * i)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
        if turtle.xcor() > 185:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("You Won")
            else:
                print("You Lost")

screen.exitonclick()
