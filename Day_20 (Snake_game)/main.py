from turtle import Screen
import time
from snake import Snake
screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to snake dungeon")
screen.setup(height=600, width=600)
screen.tracer(0)

snake = Snake()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.whole_control()


screen.exitonclick()


