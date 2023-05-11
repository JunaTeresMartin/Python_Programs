#    Author              : Juna Teres Martin
#    Last updated on     : 11/05/2023
#    Program description : Program to draw many shapes with same base

from turtle import Turtle, Screen
import random

t=Turtle()
colors=['crimson','lime green','dark turquoise','sienna','magenta','gold','lawn green']
def draw(sides):
    angle=360/sides
    for _ in range(sides):
        t.forward(80)
        t.right(angle)

for shape_side_number in range(3,11):
    t.color(random.choice(colors))
    draw(shape_side_number)
s=Screen()
s.exitonclick()