list=[]
n=int(input('Enter the number of inputs: '))
print("Enter the elements into the list")
for i in range(n):
    value=input()
    list.append(value)
target=input("Enter the value from the list to find its index: ")
if target in list:
    print(list.index(target))
else:
    print("Element not in list")