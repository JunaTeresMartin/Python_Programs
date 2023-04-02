list=[]
positive=[]
negative=[]
def separator(num):
    if num>=0:
        positive.append(num)
    else:
        negative.append(num)

n=int(input("Enter the number of elements: "))
print("Enter {} numbers".format(n))
for i in range(n):
    num=int(input())
    list.append(num)
    separator(num)
print("Positive numbers: {}".format(positive))
print("Negative numbers: {}".format(negative))