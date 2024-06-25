import numpy as np

# py function to approximate a root of a polynomial, f, bounded by a and b
# within specified tolerance (tol). |f(m)| < tol with m midpoint


def bisection(f,a,b,tol):

    if np.sign(f(a)) == np.sign(f(b)):  # check if there exists a root between a and b
        raise Exception("The scalars a and b are not bounded by a root")

    # get midpoint
    m = (a+b)/2

    if np.abs(f(m)) < tol:  # stopping condition; root found
        return m

    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection(f, m,b,tol)

    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection(f,a,m,tol)


f = lambda x: x**3 + 5*x**2 + x + 1

r1 = bisection(f, -6,-4,0.0000001)
print("First root: ", r1)
#r2 = bisection(f,0,2,0.001)
#print("Second root: ", r2)

print("r1 output: ", f(r1))
#print("r2 output:", f(r2))



