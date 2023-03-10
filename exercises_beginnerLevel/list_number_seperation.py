file=[]
positive=[]
negative=[]
f3=open("file3.txt","w")
f3=open("file3.txt","r")
n=int(input("Enter the number of integers to input: "))
print("Enter {} integers".format(n))
for i in range(0,n):
    integer=input() #read string only
    f3.write(integer+"\n")
    
    if integer>=0:
        positive.append(integer)
    else:
        negative.append(integer)
print("Positive integers in the list: ")
for i in positive:
    print(i,end=" ")
print("\nNegative integers in the list: ")
for i in negative:
    print(i,end=" ")