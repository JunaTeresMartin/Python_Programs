from turtle import Turtle,Screen
import random
color=['red','orange','yellow','green','blue','purple']
turtles=[]
s=Screen()
s.setup(width=500,height=500) #keyword arguments

for i in range(6):
    t=Turtle(shape='turtle')
    turtles.append(t)
    t.color(color[i])
    t.up()
    t.goto(-230,100-i*30)
  
user_input=s.textinput(title="Bet",prompt="Guess which color turtle is going to win the race") #a text/string value is going to be read/inputed
is_ready=False
if user_input:
    is_ready=True
while is_ready:
    for t in turtles:
        if t.xcor()>230:#250-(40/2)
            is_ready=False
            winner_color=t.pencolor()
            if winner_color==user_input:
                print("You won")
            else:
                print(f"You've lost. The {winner_color} turtle is the winner")
        distance=random.randint(0,10)
        t.forward(distance)
    