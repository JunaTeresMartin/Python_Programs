'''Scatter plots are used to show the relationships between the variables and use the dots for the plotting or it used to show the relationship between two numeric variables'''
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,1,3,4,5,6,7,8,9,10])
y=np.array([44,65,34,78,90,88,67,58,45,33])
plt.scatter(x,y)
plt.show()