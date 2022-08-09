# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 10/08/2022
# _Description_: Python program to form a right angled pattern

n=int(input("Enter the number of rows: "))
if(n<=0):
    print("Please enter a positive number >0")
for i in range (0,n):
    for j in range (0,i+1):
        print("* ",end='')
    print("\r")
