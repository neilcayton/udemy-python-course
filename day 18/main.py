# from turtle import Turtle, Screen
#
# neil = Turtle()
# neil.shape("turtle")
# neil.color("red")
# for i in range(4):
#     neil.forward(100)
#     neil.right(90)
# screen = Screen()
# screen.screensize(400,400)
# screen.exitonclick()

# import heroes
# import villains

# for i in range(20):
#     t.forward(2+2*i)
#     t.right(90)

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
