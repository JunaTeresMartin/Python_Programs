list=[]
n=int(input("Enter the number of elements: "))
print("Enter {} elements: ".format(n))

for i in range(0,n):
    element=input()
    list.append(element)
newlist=[]
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)