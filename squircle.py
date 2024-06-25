import numpy as np
import matplotlib.pyplot as plt

# x = 4sqrt(a^4-y^4)
# y = 4sqrt(a^4-x^4)

a = 1
x = np.linspace(-1,1,2000)
y = (a**4-x**4)**(1/4)

plt.plot(x,y,'k', linewidth=3)
plt.plot(x,-y,'k', linewidth=3)

plt.axis("square")
plt.axis('off')
plt.show()