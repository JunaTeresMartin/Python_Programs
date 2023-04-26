import turtle
t=turtle.Turtle()
s=turtle.Screen()

s.title("SQUARE")
t.hideturtle()
t.color('deep pink')
t.begin_fill()
t.fillcolor('deep pink')

s.bgcolor('indigo')

#logic to draw the square
for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()

s.exitonclick()