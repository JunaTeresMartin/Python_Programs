# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 14/08/2022
# _Description_: Python Program to Display Powers of 2 Using Anonymous Function


limit=int(input("Enter a limit: "))

#The map() function in Python takes in a function and a list.
# power=list(map(lambda x:x**2,range(limit)))

# for i in range(1,limit):
#     print(power[i])

power=lambda x:x**2

for i in range(1,limit+1):
    print(i,"^ 2:",power(i))
