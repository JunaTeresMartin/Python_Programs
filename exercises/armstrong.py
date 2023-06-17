# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 11/08/2022
# _Description_: Python program to check whether an n-digit integer is an Armstrong number or not.

n=int(input("Enter a number: "))
order=len(str(n))
temp=n
sum=0
while temp>0:
    remainder=temp%10
    sum=sum+(remainder**order)
    temp//=10
if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

