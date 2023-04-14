import numpy as np

np.set_printoptions(precision = 2)   # solo dos decimales
np.set_printoptions(suppress = True) # no usar notación exponencial

def sust_regre(U, b):
    # Ux = b
    n = len(b)
    x = np.zeros_like(b)    
    x[n-1] = b[n-1] / U[n-1, n-1]
    for i in range(n-2, -1, -1):
        s = 0.
        for j in range(i+1, n):
            s += U[i,j] * x[j]
        x[i] = (b[i] - s) / U[i, i]    
    return x

def triang(A,b):
    U = np.copy(A)
    c = np.copy(b)    
    n = len(b)
    for k in range(n - 1):
        for i in range(k + 1, n):
            f = U[i, k] / U[k, k]
            c[i] -= f * c[k]
            U[i] -= f * U[k]
    return U, c

A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])
b = np.array([2., 4, 6])
U, c = triang(A, b)
print('U\n', U)
print('c\n', c)
print('x\n', sust_regre(U, c))

n = 5
np.random.seed(3)           
A = np.random.random((n, n)) 
b = np.random.random(n)
U, c = triang(A, b)
print('U\n', U)
print('c\n', c)
print('x\n', sust_regre(U, c))
