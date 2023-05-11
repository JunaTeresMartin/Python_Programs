#    Author              : Juna Teres Martin
#    Last updated on     : 11/05/2023
#    Program description : Program to make a random walk with random colors

from turtle import Turtle,Screen
import random
walk=Turtle()
walk.pensize(15)
walk.speed('fastest')

directions=[0,90,180,270]

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color=(r, g, b)
    return color
for i in range(200):
    walk.color(random_color())
    walk.forward(30)
    walk.setheading(random.choice(directions))

s=Screen()
s.exitonclick()