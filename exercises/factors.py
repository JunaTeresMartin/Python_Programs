# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 05/08/2022
# _Description_: Python program to store the factors of a number into a list


def factors(num):
    flist=[]
    for i in range(1,num+1):
        if num%i==0:
            flist=flist+[i]
    print(flist)

number=int(input("Enter a number: "))
factors(number)