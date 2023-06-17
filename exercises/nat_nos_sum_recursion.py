# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 28/08/2022
# _Description_: Python Program to Find Sum of Natural Numbers Using Recursion


def rec_sum(n):
    if n<=0:
        return n
    else:
        return n+rec_sum(n-1)
    

n=int(input("Enter a number: "))
if n<=0:
    print("Enter a positive number")
else:
    print("The sum is :",rec_sum(n))



