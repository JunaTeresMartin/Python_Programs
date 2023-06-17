# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 25/07/2022
# _Description_: program to find factorial of a number

def fact(num):
    if num<0:
        print(num,"have no factorial")
    elif(num==0):
        print("factorial of 0 is 1")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial=factorial*i
        print("factorial of",num,"is",factorial)
num=int(input("Enter a number: "))
fact(num)