
#write a program to write 10 numbers into a file and find the sum of those integers
f=open("file2.txt","w")
print("Enter 10 numbers:")
for i in range(10):
    num=input()
    f.write(num+" ")
f.close()
f=open("file2.txt","r")
sum=0
for line in f:
    numlist=line.split()
    print(numlist)
    for num in numlist:
        sum+=int(num)
print(f"Sum = {sum}")
f.close()