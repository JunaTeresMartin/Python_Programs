#l= [10,12,'juna','s',3.14,"delhi",'b',"c",17,90,2.01]
# l=[["juna","johns"],"joe martin",1]
# print(len(l[0]))

#remove
l=[0,1,2,3,4,5,6,7,8,9,10,5,6,7,6,5,5,4,1]
for i in range(0,5):
    l.remove(i)
print(l)

#string to list
s="hi hello"
l=list(s)
print(l)

#append
li=[]
li.append("helooooo")
li.append(30)
print(li)

#concatenation
a=[1,2,3]
b=[4,5,6,'j']
print(a+b)

#direct convertion of string to list
print(list("list"))

#reversing a list
list1=[1,2,3,4]
print(list1[::-1])

#to find the maximum of a number
print(max(list1))  #found based on the ASCII value

#to find the minimum of a number
print(min(list1))

#insert() method
list2=["kottayam","alppuzha","ernakulam"]
list2.insert(1,"kozhikode")  #arg 1: position/index,  arg 2: value
print(list2)

print(list2[-3])

#mutator method-append()
a=[1,2,4,5,6]
b=a.append(8) #b don't return anything
print(b)  #none
print(a)  # [1, 2, 4, 5, 6, 8]