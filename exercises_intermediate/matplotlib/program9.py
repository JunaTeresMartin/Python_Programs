from matplotlib import pyplot as plt
import numpy as np
x=[5,10,15,20,25,30,35,40,45,50]
y=[1,4,3,2,5,4,6,9,8,7]
plt.plot(x,y,'r')
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(np.arange(0,51,5))
plt.yticks(np.arange(0,11,1))
plt.tick_params(axis='y',colors='r',rotation=45)
plt.show()