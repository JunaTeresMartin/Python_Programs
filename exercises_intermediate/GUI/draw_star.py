from turtle import *
t=Turtle()
t.begin_fill()
t.fillcolor('yellow')
for i in range(5):
    t.forward(200)
    t.left(144)
t.end_fill()

s=Screen()
s.exitonclick()