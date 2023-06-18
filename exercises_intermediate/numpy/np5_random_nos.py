import numpy as np
integer_array=np.random.randint(0,20,5)
print("\n\n1 D array obtained is:",integer_array)
float_array=np.random.rand(5) #generate 5 random float numbers
print("\n\n1 D float array obtained is:",float_array)
#1 d array with size m*n=3*4
new_arr=np.random.randint(1,10,(3,4))
print("\n\n1 D array with size 3*4 obtained is: ",new_arr)
#to choose a random number from numpy array
print("A random no: from the 1 D array: ",np.random.choice(integer_array))