import random
import turtle as t
t.colormode(255)

color_set = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
             (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
             (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
             (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
             (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]

# t.setheading(225)
# t.penup()
# t.forward(270)
t.penup()
t.goto(-190, -190)
t.pendown()
t.setheading(0)
t_position = t.pos()
print(t_position)
t.setheading(360)
levels = 1
for i in range(1, 100):
    dot_color = random.choice(color_set)
    t.pendown()
    t.dot(10, dot_color)
    t.penup()
    t.forward(40)
    print(i)
    if i == 10 * levels:
        t.goto(-190, -190 + 43 * levels)
        levels += 1

t.Screen().exitonclick()
