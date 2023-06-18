import matplotlib.pyplot as plt
years=[1929,1934,1977,1968,1988,2000]
runs=[23,45,89,77,99,101]
plt.plot(years,runs,'g-o',label='runs')
plt.legend()
plt.xlabel('year')
plt.ylabel('no: of runs')

plt.title("runs per years",color='blue',size=14,y=1.01,loc='left')
plt.show()