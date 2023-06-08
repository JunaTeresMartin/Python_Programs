import matplotlib.pyplot as plt
names=['A','B','C']
values=[5,20,70]
plt.figure(figsize=(9,3))

plt.subplot(131)
plt.bar(names,values)
plt.subplot(132)
plt.scatter(names,values)
plt.subplot(133)
plt.plot(names,values)
plt.suptitle('Category plotting')
plt.show()