#    Author              : Juna Teres Martin
#    Last updated on     : 11/05/2023
#    Program description : Program to make a spirograph

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw(gap):
    for n in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)
        

draw(10)