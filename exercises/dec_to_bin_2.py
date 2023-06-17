# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 28/08/2022
# _Description_: Python Program to Convert Decimal to Binary Using Recursion


def convert(n):
 if(n>=1):
   convert(n//2)
   print(n%2,end="")
   

n=34
convert(n)