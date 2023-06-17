# _author_   : Juna Teres Martin
# _File_     : gcd1.py
# _Version_  : 3.10.4
# _Date_     : 23/07/2022
# _Description_: To find the Greatest Common Factor of two numbers[using function]

def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)  #append():add to last

    fn=[]
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)

    cf=[]
    for m in fm:
        if m in fn:
            cf.append(m)

    return(cf[-1]) #returns the rightmost element
    

m=int(input("Enter the first number: "))
n=int(input("Enter the second number: "))
result=gcd(m,n)
print("The gcd of",m,"and",n,"is",result)