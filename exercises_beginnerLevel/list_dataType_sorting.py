list=[0,2,12.4,'juna','lia',3,456,45.99]
# n=int(input("Enter the number of elements: "))
# print("Enter {} elements: ".format(n))
# for i in range(0,n):
#     element=input()
#     list.append(element)
print(list)
int_list=[]
float_list=[]
str_list=[]
for i in list:
    if type(i)==int:
        int_list.append(i)
    elif type(i)==float:
        float_list.append(i)
    elif type(i)==str:
        str_list.append(i)
print(int_list)
print(float_list)
print(str_list)