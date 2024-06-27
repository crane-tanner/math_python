import matplotlib.pyplot as plt
import sympy as sym

x = sym.symbols('x')
y = x**2 - 3*x

for i in range(-11,11):
    plt.plot(i, y.subs(x, i), 'o')

plt.xlabel('x')
plt.ylabel('f(x)=x^2-3x')
plt.show()