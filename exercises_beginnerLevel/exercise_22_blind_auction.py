#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Write a program that finds how gave the highest bid in the blind auction
#DATE     :  16-03-2023

# >>The screen is cleared after each input


import os
from art import auction
print(auction)
auctioning_details={}
next=True
while next:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    choice=input("Are there any other bidders? Type 'yes' or 'no'.")
    auctioning_details[name]=bid
    if choice=='yes':
       os.system('cls')

    elif choice=='no':
        largest=0
        for key in auctioning_details:
            if auctioning_details[key]>largest:
                largest=auctioning_details[key]
                winner=key
        print(f"The winner is {winner} with a bid of ${largest}")
        next=False

    else:
        print("Please choose 'yes' or 'no'")
        