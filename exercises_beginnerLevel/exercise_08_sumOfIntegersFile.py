f=open("integers.txt","w")
sum=0
print("Enter 10 numbers:")
for i in range(10):
    num=input()
    f.write(num)
    sum+=int(num.strip("\n"))

print(f"Sum = {sum}")
f.close()