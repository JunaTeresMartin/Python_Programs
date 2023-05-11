#    Author              : Juna Teres Martin
#    Last updated on     : 11/05/2023
#    Program description : Program to make a random walk

from turtle import Turtle,Screen
import random
walk=Turtle()
colors=['medium slate blue','medium sea green','lime','deep pink']
directions=[0,90,180,270]

walk.pensize(15)
walk.speed('fastest')
for i in range(200):
    walk.color(random.choice(colors))
    walk.forward(30)
    walk.setheading(random.choice(directions))

s=Screen()
s.exitonclick()