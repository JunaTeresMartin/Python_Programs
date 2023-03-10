list=[]
n=int(input("Enter the number of values: "))
for i in range(n):
    list.append(input())
list.sort()
freq=0
freq=[]
larger=0
for i in range (0,n):
    freq=0
    for j in range (0,n):
        if int(list[i])==int(list[j]):
            freq+=1
        freq.insert(n,freq)
    
print(max(freq))
 