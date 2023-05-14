#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that creates a keyboard controlled sketch game
#DATE     :  14-05-2023


from turtle import Turtle,Screen
t=Turtle()
s=Screen()

def forwards():
    t.forward(30)
def backwards():
    t.backward(30)
def counter_clockwise():
    t.circle(-30)
def clockwise():
    t.circle(30)
def turn_left():
    new_heading=t.heading()+30
    t.setheading(new_heading)
def turn_right():
    new_heading=t.heading()-30
    t.setheading(new_heading)
def clear_screen():
    # s.clear()  [This will clear everything in the screen including the pen, so after this dcreen clearning we can't draw anymore]
    t.clear() #this only clears the turtle (the drawn things)
    t.up()
    t.home()
    t.down()
    

s.listen()
s.onkey(forwards,"Up")
s.onkey(backwards,"Down")
s.onkey(counter_clockwise,"a")
s.onkey(clockwise,"l")
s.onkey(turn_left,"Left")
s.onkey(turn_right,"Right")
s.onkey(clear_screen,"c")
s.exitonclick()