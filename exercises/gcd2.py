# _author_   : Juna Teres Martin
# _File_     : gcd2.py
# _Version_  : 3.10.4
# _Date_     : 23/07/2022
# _Description_: To find the Greatest Common Factor of two numbers[using built-in function]

import math
m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
result=math.gcd(m,n)
print("The gcd of",m,"and",n,"is",result)