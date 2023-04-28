from turtle import *
t=Turtle()

def draw(color,x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(30)
    t.end_fill()
    t.up()
    t.home()
    t.down()

draw('red',0,5)
draw('green',200,200)
s=Screen()
s.exitonclick()