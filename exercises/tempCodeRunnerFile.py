def reccu_fibu(n):
    if n<=1:
        return n;
    else:
        return reccu_fibu(n-1)+reccu_fibu(n-2);
for i in range(10):
    print(reccu_fibu(i));