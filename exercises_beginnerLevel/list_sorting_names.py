n=int(input("Enter the number of names: "))
print("Enter the names : ")
#l=list("") #defining the string list
#or
l=[]
print("Enter {} names".format(n))
for i in range(0,n):
    name=input()
    l.append(name)
l.sort()
print("Names sorted in alphabetic order: ")
print(l)
for i in l:
    print(i)