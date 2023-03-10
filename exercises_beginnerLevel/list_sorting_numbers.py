list=[]
n=int(input("Enter the number of values: "))
for i in range(n):
    list.append(int(input()))
for i in range(0,n):
    for j in range(0,n-1-i):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("Numbers after sorting: ")  
for i in list:
    print(i,end=" ")         
