from turtle import Turtle,Screen

#game body
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.title('Snake Game')

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
    for seg in segments:
        seg.forward(20)



s.exitonclick()