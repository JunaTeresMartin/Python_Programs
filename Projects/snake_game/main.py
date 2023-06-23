from turtle import Turtle,Screen
import time
#game body
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.title('Snake Game')
s.tracer(0)#Turn turtle animation on/off and set delay for update drawings

#snake
#turtle default size 20*20
starting_positions=[(0,0),(-20,0),(-40,0)]

segments=[]
for position in starting_positions:
    new_segment=Turtle("square")
    new_segment.penup()
    segments.append(new_segment)
    new_segment.color("white")
    new_segment.goto(position)

is_game_on=True
while(is_game_on):
    s.update()
    time.sleep(0.01)
    for seg in range(len(segments),0,-1):
        new_x=segments[seg-1].xcor()
        new_y=segments[seg-1].ycor()
        segments[seg].goto(new_x,new_y)
    segments[0].forward(20)
    segments[0].left(90)


s.exitonclick()