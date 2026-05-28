import numpy as np

def gauss_seidel_profesional(A, b, x0=None, tol=1e-7, max_iter=100):
    n = len(A)
    if x0 is None: x0 = np.zeros(n)
    x = x0.copy()
    
    print("Iniciando Gauss-Seidel...")
    for k in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
            
        error = np.linalg.norm(x - x_old, np.inf) / np.linalg.norm(x, np.inf)
        if error < tol:
            print(f"Éxito en iteración {k}")
            return x
    return x

A = np.array([[10, -1, 2], [-1, 11, -1], [2, -1, 10]], dtype=float)
b = np.array([6, 25, -11], dtype=float)
print("Solución GS:", gauss_seidel_profesional(A, b))

#Salida
#Éxito en iteración 6
#Solución GS: [ 1.04326923  2.26923077 -1.08173077]