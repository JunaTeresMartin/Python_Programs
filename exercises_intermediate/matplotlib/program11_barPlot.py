import matplotlib.pyplot as p
import numpy as n
x=n.array(['S','A+','A','B+','B'])
y=n.array([12,22,20,13,12])
p.title('python programming')
p.xlabel('no of students')
p.ylabel('grades')
p.bar(x,y,color='r')
p.barh(x,y,color='g')
p.show()
