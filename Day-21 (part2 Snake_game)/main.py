from turtle import Screen
from scoreboard import Scoreboard
import time
from foodie import Food
from snake import Snake
screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to snake dungeon")
screen.setup(height=600, width=600)
screen.tracer(0)
food = Food()
snake = Snake()
snake_score = Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.whole_control()
    if snake.segment[0].distance(food) < 15:
        screen.update()
        food.generate_loc()
        snake.add_len()
        print(snake.snake_body_count)
        snake_score.increase_scoreboard()
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 280 or snake.segment[0].ycor() < -280:
        game_is_on = False
        snake_score.game_over()

screen.exitonclick()


