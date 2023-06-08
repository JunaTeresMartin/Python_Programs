import matplotlib.pyplot as p
import numpy as np
import math
x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
p.plot(x,y)
p.xlabel("angle")
p.ylabel("sine")
p.title("Sine Wave")
p.show()
