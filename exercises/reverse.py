# Write a program to reverse a number and reverse a string.

num = 4586644;
str = "hello meeee";

print(str[::-1]);
new_num=0
while(num!=0):
    r = num%10;
    num=num//10;
    new_num = r + new_num * 10
print(new_num);



#fibinocci series using recursion
def reccu_fibu(n):
    if n<=1:
        return n;
    else:
        return reccu_fibu(n-1)+reccu_fibu(n-2);
for i in range(10):
    print(reccu_fibu(i));