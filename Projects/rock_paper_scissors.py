#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that creates the game rock-paper-scissors
#DATE     :  08-03-2023


#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
print("0: rock\n1: paper\n2: scissors")
print("Choose 0/1/2: ")
your_choice=int(input())
computer=random.randint(0,2)
if your_choice==0:
    print("you:")
    print(rock)
    if computer==0:
            print("computer:")
            print(rock)
            print("\ndraw")
    elif computer==1:
            print("computer:")
            print(paper)
            print("\nYou lose")
    elif computer==2:
            print("computer:")
            print(scissors)
            print("\nYou won")
elif your_choice==1:
    print("you:")
    print(paper)
    if computer==0:
            print("computer:")
            print(rock)
            print("\nYou won")
    elif computer==1:
            print("computer:")
            print(paper)
            print("\ndraw")
    elif computer==2:
            print("computer:")
            print(scissors)
            print("\nYou lose")
elif your_choice==2:
    print("you:")
    print(scissors)
    if computer==0:
            print("computer:")
            print(rock)
            print("\nYou lose")
    elif computer==1:
            print("computer:")
            print(paper)
            print("\nYou won")
    elif computer==2:
            print("computer:")
            print(scissors)
            print("\ndraw")
else:
       print("Invalid choice. Please choose between 0-2")      