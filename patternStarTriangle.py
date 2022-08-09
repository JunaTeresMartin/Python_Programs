# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 09/08/2022
# _Description_: Python program to print star pattern in triangle form

n=int(input("Enter the number of rows: "))
m=n-1
for i in range(0,n):
    for j in range (0,m):
        print(end=" ")
    m-=1
    for  k in range(0,i+1):
        print("* ",end='')
    print("\r")
        
      
