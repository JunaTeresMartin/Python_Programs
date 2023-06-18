from numpy import array
import numpy as np
arr1=array([11,62,3,14])
arr2=array([2,4,7,6])
#addition
# print(arr1+arr2)
print(np.add(arr1,arr2))

#subtraction
# print(arr1-arr2)
print(np.subtract(arr1,arr2))

#multiplication
# print(arr1*arr2)
print(np.multiply(arr1,arr2))

#division
# print(arr1/arr2)
print(np.divide(arr1,arr2))

#mod or remainder
print(np.remainder(arr1,arr2))
print(np.mod(arr1,arr2))

#power function
print(np.power(arr1,arr2))