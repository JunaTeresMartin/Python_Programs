from turtle import *
t=Turtle()

def draw(x,y,color):
    
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(30)
    t.end_fill()
    #t.home()

draw(0,30,'red')
draw(60,30,'green')
draw(120,30,'yellow')
draw(180,30,'purple')
s=Screen()
s.exitonclick()
