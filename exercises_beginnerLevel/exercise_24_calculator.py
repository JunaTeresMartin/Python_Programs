#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to build a calculator
#DATE     :  16-03-2023

from art import calculator
print(calculator)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operators={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

n1=float(input("Enter first number: "))
n2=float(input("Enter second number: "))
#prints the symbols
for symbol in operators:
    print(symbol)
your_symbol=input("Choose an operational symbol: ")
#takes the values of the key(symbol)
sym=operators[your_symbol]
result=sym(n1,n2)
print(f"{n1} {your_symbol} {n2} = {result}")
continuing=input(f"Continuing calculation with {result}, y for yes, n for no: ")
while continuing== 'y':
    your_symbol=input("Choose an operational symbol: ")
    sym=operators[your_symbol]
    n2=float(input("Enter next number: ")) 
    result2=sym(result,n2)
    print(f"{result} {your_symbol} {n2} = {result2}")
    result=result2
    continuing=input(f"Continuing calculation with {result2}, y for yes, n for no: ")

