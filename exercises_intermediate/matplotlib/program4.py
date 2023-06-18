import numpy as np
import matplotlib.pyplot as plt
 #plot 1
x=np.array([0,1,2,3])
y=np.array([4,8,0,12])
plt.subplot(2,1,1)
plt.plot(x,y,'o-')
plt.grid(True)

 #plot 2
x=np.array([0,1,2,3])
y=np.array([10,12,20,30])
plt.subplot(2,1,2)
plt.plot(x,y,'o-')
plt.grid(True)

plt.show() 