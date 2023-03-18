#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that creates the BlackJack/21 game
#DATE     :  18-03-2023

#Rules
"""
$ The deck is unlimited in size. 
$ There are no jokers. 
$ The Jack/Queen/King all count as 10.
$ The the Ace can count as 11 or 1.
$ Use the following list as the deck of cards:
$ cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
$ The cards in the list have equal probability of being drawn.
$ Cards are not removed from the deck as they are drawn.
$ The computer is the dealer.
"""
import random
import os
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(player):
  score_sum=sum(player)
  if score_sum==21 and len(player)==2:
    return 0
  if score_sum>21 and 11 in player:
        player.remove(11)
        player.append(1)
  return score_sum
def compare(user_score,computer_score):
    if computer_score==user_score:
      return ("draw")
    elif computer_score==0:
      return "User lose, opponent has BlackJack"
    elif user_score==0:
      return "win with a BlackJack"
    elif computer_score>21:
      return "Opponent went over, You win"
    elif user_score>21:
      return "You went over, you lose"
    elif computer_score>user_score:
      return "Computer wins"
    elif computer_score<user_score:
      return ("User wins")


while(input("Do yo want to play BlackJack, 'y' or 'n': ")=='y'):
  os.system('cls')
  from art import blackjack
  print(blackjack)
  user_cards = []
  computer_cards = []
  game_over=False
  
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over: 
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
  
    print(f"Your card {user_cards}, score: {user_score}")
    print(f"computer first card {computer_cards[0]}")
    
    # if we got a blackJack or score>21
    if computer_cards==0 or user_score==0 or user_score>21:
      game_over=True
    else:
      choice=input("Enter 'y' for next card, 'n' to pass: ")
      if choice=='y':
         user_cards.append(deal_card())
      else:
        game_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(f"Final user cards: {user_cards}, Final user score: {user_score}")
  print(f"computer cards: {computer_cards}Computer score: {computer_score}")
  print(compare(user_score, computer_score))
  







