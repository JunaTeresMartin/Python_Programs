# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 13/08/2022
# _Description_: Python Program to Find the Sum of n Natural Numbers

n=int(input("Enter a limit: "))
limit=n
sum=0
if(n<0):
    print("Enter a positive number")
else:
    while(n>0):
        sum=sum+n
        n-=1

    print("The sum of",limit,"natural numbers is",sum)
