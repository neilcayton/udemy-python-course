import turtle
# for i in range(8):
    # turtle.stamp(); turtle.fd(30)
    # turtle.clearstamps(2)
    # turtle.clearstamps(-2)
    # turtle.clearstamps()
    # turtle.goto(10, 10)
    # turtle.towards(0, 0)


# t.pos()
# turtle.goto(10, 10)
# t.towards(0,0)
TURTLE_SIZE = 20
turtle.home()
turtle.setposition(10, 30)
turtle.left(130)
turtle.goto(-50,-50)
turtle.forward(100)
t_position = turtle.pos()
t_heading = turtle.heading()
t_screen = turtle.Screen()
turtle.goto(TURTLE_SIZE/2 - t_screen.window_width()/2, t_screen.window_height()/2 - TURTLE_SIZE/2)
print(f"position: {t_position}\n"
      f"heading: {t_heading}\n"
      f"t_screen: w-{t_screen.window_width()}, l{t_screen.window_height()}")
print(round(turtle.xcor(), 5))



turtle.Screen().exitonclick()

