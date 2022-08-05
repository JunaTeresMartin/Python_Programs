# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 05/08/2022
# _Description_: Python Program to check whether a number is odd or even

def divides(m,n):
    if(m%n)==0:
        return(True)
    else:
        return(False)

def even(num):
    return(divides(num,2))

m=int(input("Enter a number: "))
if (even(m) ):
    print(m,"is even") 
else:
    print(m,"is odd")