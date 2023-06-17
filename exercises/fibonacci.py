# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 09/08/2022
# _Description_: Python program to print fibonacci numbers

def fibonacci(n):
    first=0
    second=1
    third=0
    while(third<n):
        print(first)
        third=first+second
        first=second
        second=third

n=int(input("Enter a limit: "))
fibonacci(n)