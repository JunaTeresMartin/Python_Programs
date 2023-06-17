# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 16/08/2022
# _Description_: Python Program to Find Numbers Divisible by Another Number

n=int(input(("Enter the number of elements: ")))
print("Enter the numbers: ")
mylist=[]
for i in range(0,n):
    element=int(input())
    mylist.append(element)

divisor=int(input("Enter a number to find its divisibility: "))
result=list(filter(lambda x:(x%divisor==0),mylist))
print("The numbers divisible by",divisor,"in the list are",result)