import matplotlib.pyplot as plt
import numpy as np
# y = mx + b

x1 = [-5,5]
m1 = 0.7
b1 = -2

x2 = [-5,5]
m2 = -1.25
b2 = 0.75

#y = [340,2345]

#for i in range(0, len(x)):
    #y[i] = m*x[i] + b

y1 = m1*np.array(x1) + b1
y2 = m2*np.array(x2) + b2
plt.plot(x1, y1, label = 'y=%sx + %s'%(m1,b1))
plt.plot(x2, y2, label = 'y=%sx + %s'%(m2,b2))

plt.axis('square')
plt.grid()
plt.xlim(x1)
plt.ylim(x1)

plt.plot([0,0], [-5,5], 'k--') # vertical
plt.plot([-5,5], [0,0], 'k--') # horizontal

plt.legend()
plt.title('The plot')
plt.show()