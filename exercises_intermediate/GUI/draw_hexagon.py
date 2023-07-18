from turtle import *
t=Turtle()
t.pensize(10)
t.pencolor('yellow')
t.begin_fill()
t.fillcolor('red')
for i in range(6):
    t.forward(100)
    t.left(60)
t.end_fill()
s=Screen()
s.exitonclick()