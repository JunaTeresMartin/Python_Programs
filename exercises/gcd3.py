# _author_   : Juna Teres Martin
# _File_     : gcd3.py
# _Version_  : 3.10.4
# _Date_     : 23/07/2022
# _Description_: To find the Greatest Common Factor of two numbers


def gcd(a,b):
    for i in range(1,min(a,b)+1):
        if (a%i==0) and (b%i==0):
            gcd=i
    print(i,"is the greatest common factor of",a,"and",b)

number1=int(input("Enter number 1:"))
number2=int(input("Enter number 2:"))
gcd(number1,number2)