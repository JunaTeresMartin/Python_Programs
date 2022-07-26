# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 26/07/2022
# _Description_: Python Program to Generate a Random Number within a limit

import random

list=['a','s',3,6,34,'f']
print("random element selected from the list is",random.choice(list))
a=int(input("Enter starting limit: "))
b=int(input("Enter ending limit: "))

print(random.randint(a,b))