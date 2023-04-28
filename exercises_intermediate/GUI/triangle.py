from turtle import *
t=Turtle()
t.hideturtle()
t.begin_fill()
t.fillcolor('green')
for i in range(3):
    t.forward(i*200-100)
    t.left(120)

t.end_fill()

s=Screen()
s.exitonclick()