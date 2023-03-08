#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to find who will pay the bill
#DATE     :  08-03-2023

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
# Import the random module
import random
l=len(names)
person=random.randint(0,l-1)
print(names[person] + " is going to buy the meal today!")

#OR
# another option is using choice()- so we have only less code
name=random.choice(names)
print(name + " is going to buy the meal today!")