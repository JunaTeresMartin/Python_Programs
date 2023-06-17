# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 13/08/2022
# _Description_: Python program to print all armstrong numbers in an interval

def armstrong(a,b):
    order1=len(str(a))
    order2=len(str(b))
    for i in range(a,b+1):
        sum=0
        temp=i
        while temp>0:
            rem=temp%10
            sum=sum+rem**len(str(i))
            temp//=10
        if sum==i:
            print(i)

a=int(input("Enter starting number: "))
b=int(input("Enter ending number: "))
armstrong(a,b)

        
