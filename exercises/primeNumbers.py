# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 06/08/2022
# _Description_: Python program to print the prime numbers in a range

def primes(m,n):
    for i in range(m,n+1):
        flag=0
        for j in range(2,int((m+n)/2)):
            if i!=j:
               if i%j==0:
                   flag=flag+1
                   break
        if(flag==0):
            print(i)


m=int(input("number 1: "))
n=int(input("number 2: "))
primes(m,n)