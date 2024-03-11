#  Write a function to print the Fibonacci series
def fibu(n):
    a = 0;
    b = 1;
    for i in range(n):
        print(a);
        c = a + b;
        a = b;
        b = c;
fibu(10);


my_array = [64, 25, 12, 22, 11]
n=len(my_array);
for i in range(n):
    for j in range(n-1-i):
        if my_array[j+1]<my_array[j]:
            my_array[j+1],my_array[j]=my_array[j],my_array[j+1];
print(my_array);


n=20
for i in range(2,n):
    flag=0
    for j in range(2,i//2):
        if (i%j==0):
            flag=1
            break
    if flag==0:
        print(i,end=" ")

    