from numpy import array,trace
from numpy.linalg import inv
a=array([[1,2],[3,4]])
print(inv(a))
print(a.dot(inv(a)))
print(trace(a))