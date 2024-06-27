import matplotlib.pyplot as plt

#x = [1,4,6,-2,3]
#y = [5,6,-5,3,9]
#for i in range(0, len(x)):
   # plt.plot(x[i], y[i], 'o', label ='point %s' %i)

#plt.axis('square')
#plt.grid()
#plt.legend()
#plt.show()

plt.plot(4,2,'k+')
plt.grid()
axis = plt.gca()
ylim = axis.get_ylim()
print(ylim)
axis.set_ylim(0.0, 5.2)


plt.show()