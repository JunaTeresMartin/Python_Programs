def fib(a,b,n):
    c=a+b
    if a==n:
        print(a)
    else:
        a=b
        b=c
        fib(a,b,n)

a=0
b=1
n=4
fib(a,b,n)