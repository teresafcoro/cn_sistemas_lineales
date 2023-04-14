import numpy as np

np.set_printoptions(precision = 2)   # dos decimales
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

U = np.array([[2., 1, 1], [0, 2, 1], [0, 0, 2]]) # matriz triangular superior
b = np.array([9., 4, 4]) # matriz columna
print('x\n', sust_regre(U,b))

n = 5
np.random.seed(2)           
U = np.random.random((n, n)) 
U = np.triu(U) # Haz cero los elementos bajo la diagonal
b = np.random.random(n)
print('x\n', sust_regre(U, b))
