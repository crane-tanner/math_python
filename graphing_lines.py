import matplotlib.pyplot as plt
import numpy as np

# y = sqrt(abs(x)))
x = range(-21, 21)

for xi in x:
    plt.plot([0,xi], [0,np.sqrt(abs(xi))])


plt.grid()
plt.axis('square')
axis = plt.gca()
axis.set_ylim(0,5)

plt.show()