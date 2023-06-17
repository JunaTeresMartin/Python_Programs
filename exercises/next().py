# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 26/07/2022
# _Description_: Python Program to implement built-in function next()

list=['abin','noel','tomy',45.5,900]


# convert list to iterator
iterator_list = iter(list)

value1=next(iterator_list)
print("First element: ")
print(value1)

value2=next(iterator_list)
print("Second element: ")
print(value2)

value3=next(iterator_list)
print("Third element: ")
print(value3)

value4=next(iterator_list)
print("Fourth element: ")
print(value4)

value5=next(iterator_list)
print("Fifth element: ")
print(value5)



# This will create error
# value6=next(iterator_list)
# print("Next element: ")
# print(value6)