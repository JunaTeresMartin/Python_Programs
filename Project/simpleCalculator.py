import math

#function for addition operation
def add(x,y):
  print(x+y)

#function for subtraction operation
def sub(x,y):
  print(x-y)

#function for multiplication operation
def mul(x,y):
  print( x*y)

#function for division operation
def div(x,y):
  if y==0:
    print("Invalid division")
  else:
    print(x/y)

#function for exponent operation
def pwr(x,y):
  print(x**y)

#function for logarithm operation
def log(x,y):
  print (math.log(x,y)) 

#function for natural logarithm operation
def nlog(x):
  print (math.log(x))

# returns the factorial value
def fact(n):
    if n == 0:
        return 1
    res = 1
     
    for i in range(2, n+1):
        res = res * i
         
    return res

#function for nCr
def nCr(n, r):
 
    print (fact(n) / (fact(r)
                * fact(n - r)))

#function for nPr
def nPr(n, r):
    print(fact(n)/fact(n-r))

#function for exponent
def exp(x):
    print(math.exp( x ))
   
#invalid operation
def default(x,y):
  return "Invalid Operation"
choice="y"
while (choice=='y'):
  
    print('''
             1.Addition
             2.Subtraction
             3.Multiplication
             4.Division
             5.x^n
             6.logarithm
             7.natural logarithm
             8.nCr
             9.nPr
             10.e^x
             ''')
    print("Enter your choice: ")
    choice=int(input())
    if(choice==1):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        add(x,y)
    elif(choice==2):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        sub(x,y)
    elif(choice==3):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        mul(x,y)
    elif(choice==4):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        div(x,y)
    elif(choice==5):
        x=int(input("Enter first number: "))
        y=int(input("Enter second number: "))
        pwr(x,y)
    elif(choice==6):
        x=int(input("Enter a number: "))
        y=int(input("Enter the base: "))
        log(x,y)
    elif(choice==7):
        x=int(input("Enter a number: "))
        nlog(x)
    elif(choice==8):
        x=int(input("Enter n: "))
        y=int(input("Enter r: "))
        nCr(x,y)
    elif(choice==9):
        x=int(input("Enter n: "))
        y=int(input("Enter r: "))
        nPr(x,y)
    else:
        x=int(input("Enter a number: "))
        exp(x)



  #continue the operations or not
    choice=input("do you want to continue(y/n): ")
    
