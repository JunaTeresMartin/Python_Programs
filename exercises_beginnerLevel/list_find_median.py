list=[]
n=int(input("Enter the number of values: "))
for i in range(n):
    list.append(input())
list.sort()
if n%2==0:
    average=(int(list[(n//2)-1])+ (int(list[n//2])))/2
    print(f"Median= {average}")
else:
    print(f"Median= {list[n//2]}")
