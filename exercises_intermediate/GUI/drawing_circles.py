import turtle
t=turtle.Turtle()
s=turtle.Screen()

s.title("CIRCLES")
t.hideturtle()
t.color('deep pink')

s.bgcolor('indigo')

#logic to draw the circle
t.circle(100)
t.circle(-100)
t.left(90)
t.circle(100)
t.circle(-100)
t.left(45)
t.circle(100)
t.circle(-100)
t.left(90)
t.circle(100)
t.circle(-100)

s.exitonclick()