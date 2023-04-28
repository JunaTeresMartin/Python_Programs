from turtle import *
t=Turtle()
t.speed(9)


for i in range(10,1,-1):
    t.begin_fill()
    t.fillcolor('red')
    t.circle(i*10)
    t.circle(-i*10)
    t.end_fill()

    t.left(45)
    t.begin_fill()
    t.fillcolor('blue')
    t.circle(i*10)
    t.circle(-i*10)
    t.end_fill()

    t.left(45)
    t.begin_fill()
    t.fillcolor('green')
    t.circle(i*10)
    t.circle(-i*10)
    t.end_fill()

    t.left(45)
    t.begin_fill()
    t.fillcolor('yellow')
    t.circle(i*10)
    t.circle(-i*10)
    t.end_fill()


s=Screen()
s.exitonclick()