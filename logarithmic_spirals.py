import numpy as np
import matplotlib.pyplot as plt

# x = cos(t)e^(t/k)
# y = sin(t)e^(t/k)

N = 150
t = np.linspace(0, 10*np.pi, 1234)
k = np.linspace(-6, -2, N)

for i in range(N):
    x = np.cos(t)*np.exp(t/k[i])
    y = np.sin(t)*np.exp(t/k[i])
    plt.plot(x, y, color=[i/N,i/N,0])


plt.axis('square')
plt.axis('off')
plt.show()
