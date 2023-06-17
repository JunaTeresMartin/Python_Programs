# _author_     : Juna Teres Martin
# _Version_    : 3.10.4
# _Date_       : 16/08/2022
# _Description_: Python Program to find the L.C.M. of two input number



def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True): 
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1 #the maximun for greater is num1*num2

   return lcm

num1 = int(input("number1: "))
num2 = int(input("number2: "))

print("\nThe L.C.M. is", compute_lcm(num1, num2))