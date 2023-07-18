from numpy import array
a=array([[1,2],[5,9],[10,11]])
b=array([[4,1,2],[0,2,3]])
print(a.ndim)  #number of columns in array a
print(b.ndim)
print(a.dot(b))