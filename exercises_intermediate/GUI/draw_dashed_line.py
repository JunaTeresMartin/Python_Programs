#    Author              : Juna Teres Martin
#    Last updated on     : 11/05/2023
#    Program description : Program to draw a dashed line


from turtle import Turtle, Screen
t=Turtle()
for i in range(30):
    t.pd() #pen down
    t.forward(5)
    t.pu() #pen up
    t.forward(5)
    

s=Screen()
s.exitonclick()