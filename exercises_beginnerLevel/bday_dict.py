birthdays={}
n=int(input("Enter the number of inputs: "))
print("Input {} names and their bithdays".format(n))
for i in range (n):
    name=input("Name: ")
    birthday=input("Birthday: ")
    birthdays[name]=birthday

name=input("Enter a name whose b'day you want to know: ")
bday=birthdays[name]
print(name,"'s birthday is on",bday)