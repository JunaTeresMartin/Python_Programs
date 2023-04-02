#min_max function that takes n numbers as list arguments and return the largest and smallest numbers
def min_max(list):
    maximum=max(list)
    minimum=min(list)
    return maximum,minimum

list1=[]
n=int(input("Enter the number of inputs: "))
print("Enter {} numbers".format(n))
for i in range (n):
    list1.append(int(input()))
mini,maxi=min_max(list1)
print(f"Maximum= {maxi}\nMinimum= {mini}")
