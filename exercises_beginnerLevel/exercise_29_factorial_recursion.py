#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program to build a factorial function using recursion
#DATE     :  04-04-2023

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
n=int(input("Enter a number: "))
factorial=fac(n)
print("Factorial= ",factorial)