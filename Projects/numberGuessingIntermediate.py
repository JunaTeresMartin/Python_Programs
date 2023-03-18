art="""

   ____                       _   _                                  _               
  / ___|_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                                                                                                         
"""
import random
number=random.randint(1,100)
difficulty=input("Choose a difficulty. 'e' for easy and 'h' for hard: ")
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nCan you guess it???")
if difficulty=='e':
    attempts=10
    compare=attempts
else:
    attempts=5
    compare=attempts
print(number)
i=1
while i<=attempts:
    print(f"You have {i} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess>number and guess-number>=compare:
        print("Too high")
    elif guess<number and number-guess>=compare:
        print("Too low")
    elif guess<number and number-guess<compare:
        print("Low but near")
    elif guess>number and guess-number<compare:
        print("High but near")
    elif guess==number:
        print("Awesome! Your answer is correct")
        break #this break is powerful
    if i==attempts: #should be added last
        print("Sorry! You lose.")
    i+=1
    
    
