#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Program demonstrating short circuit evaluation of python interpreter
#LAST DATE MODIFIED  :  24-03-2023

'''
The Python virtual machine sometimes knows the value of a Boolean expression before it has evaluated all of its operands. 

For instance, in the expression A and B, if A is false, then so is the expression, and there is no need to evaluate B.

Likewise, in the expression A or B, if A is true, then so is the expression, and again there is no need to evaluate B. 

This approach, in which evaluation stops as soon as possible, is called short-circuit evaluation.

'''

count = int(input("Enter the count: ")) #input 10
theSum = int(input("Enter the sum: ")) #input 45
if count > 0 or theSum // count > 10: #count is greater than 0(true), so interpreter don't check the second part
	print("average > 10")
else:
	print("count = 0 or average <= 10")

