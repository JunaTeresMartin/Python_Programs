import turtle
t=turtle.Turtle()
t.speed(0)
t.fillcolor('orange')
t.begin_fill()
for i in range(5):
    t.circle(90,90)
    t.left(90)
    t.circle(90,90)
    t.left(18)
t.end_fill()