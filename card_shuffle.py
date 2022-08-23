# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 23/08/2022
# _Description_: Python Program to Shuffle Deck of Cards

import itertools,random

# make a deck of cards
deck=list(itertools.product(range(1,13),['Spade','Heart','Diamond','Club']))

#shuffle the cards
random.shuffle(deck)

#draw two cards
print("Taking 2 cards!!!!\n")
print("you got: ")
for i in range(2):
    print(deck[i][0],"of",deck[i][1])

