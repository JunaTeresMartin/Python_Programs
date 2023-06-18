import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr[4:])#from index 4 onwards
print(arr[:4])#upto index 4
print(arr[-3:-1])
print(arr[0:7:2])

arr2d=np.array([[3,4,5,6],[3,9,8,7]])
print(arr2d[1:,1:3])
#transpose
print(np.transpose(arr2d))