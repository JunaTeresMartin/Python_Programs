# import colorgram #colorgram.py is a Python library that lets you extract colors from images.
# colors = colorgram.extract('image.jpg', 30) #30 is the no: of colors to be extracted
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
import turtle as t
import random
dot_turtle = t.Turtle()
t.colormode(255)

dot_turtle.pu()
dot_turtle.goto(-130,-130)
dot_turtle.pd()

#dot_turtle.setheading(0)
for i in range(10):
    dot_turtle.pu()
    dot_turtle.goto(-130, -130+i*30)
    dot_turtle.pd()
    for j in range(10):
        dot_turtle.dot(10, random.choice(colors))
        dot_turtle.pu()
        dot_turtle.forward(30)
        dot_turtle.pd()

s=t.Screen()
s.exitonclick()





