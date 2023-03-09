#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  A program that creates a Password Generator 
#DATE     :  09-03-2023

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= random.randint(1,5)
nr_symbols = random.randint(1,5)
nr_numbers = random.randint(1,5)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password1="" #we are using a string
for i in range(0,nr_letters):
    l=random.choice(letters)
    password1+=l
for i in range(0,nr_symbols):
    n=random.choice(numbers)
    password1+=n
for i in range(0,nr_symbols):
    s=random.choice(symbols)
    password1+=s
print(f"\nEasy password: {password1}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password2=[]  #we are using a list
for i in range(0,nr_letters):
    l=random.choice(letters)
    password2.append(l)
for i in range(0,nr_symbols):
    n=random.choice(numbers)
    password2.append(n)
for i in range(0,nr_symbols):
    s=random.choice(symbols)
    password2.append(s)

#shuffling the values using shuffle method
random.shuffle(password2)
p=""
for i in password2:
    p+=i

print(f"\nHard password: {p}")