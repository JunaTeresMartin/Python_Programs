# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 24/08/2022
# _Description_: Python Program to Display Fibonacci Sequence Using Recursion


from cmath import rect


def rec_fib(n):
    if(n<=1):
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)


n=int(input("Enter the number of terms: "))
if(n<=0):
    print("Enter a positive number")
else:
    print("The Fibonacci series: ")
    for i in range(n):
        print( rec_fib(i))

   