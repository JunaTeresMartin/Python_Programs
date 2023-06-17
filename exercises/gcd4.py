# _author_     : Juna Teres Martin
# _File_       : gcd4.py
# _Version_    : 3.10.4
# _Date_       : 23/07/2022
# _Description_: To find the Greatest Common Factor of two numbers


def gcd(a,b):
    i=min(a,b)
    while i>0:
        if (a%i==0) and (b%i==0):
            return(i) #explicity get exit if we get the answer
        else:
            i=i-1
    

number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))
gcd=gcd(number1,number2)
print(gcd,"is the greatest common factor of",number1,"and",number2)