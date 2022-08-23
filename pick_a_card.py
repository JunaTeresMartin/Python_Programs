# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 23/08/2022
# _Description_: Python program to select a random card in Python from a deck of cards

import random

#assigning the card points
random_point=['A',2,3,4,5,6,7,8,9,'J','Q','K']

#assigning the card symbols
random_symbol=['Heart','Diamond','Club','Spade']

#ransom choose of point
point=random.choice(random_point)

#random choose of symbol
symbol=random.choice(random_symbol)

#random selection of a point and symbol
card=point,symbol

#display the card
print("Your card is",card)
