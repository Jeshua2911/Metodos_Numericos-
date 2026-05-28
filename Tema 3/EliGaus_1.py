import numpy as np

def eliminacion_gaussiana(A, b):
    n = len(b)
    # Matriz aumentada
    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)

    # Eliminación hacia adelante
    for i in range(n):
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] - factor * Ab[i]

    # Sustitución hacia atrás
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i][-1] - np.dot(Ab[i][i+1:n], x[i+1:n])) / Ab[i][i]
    
    return x

# Ejemplo: 3x + 2y - z = 1; 2x - 2y + 4z = -2; -x + 0.5y - z = 0
A = np.array([[3.0, 2.0, -1.0], [2.0, -2.0, 4.0], [-1.0, 0.5, -1.0]])
b = np.array([1.0, -2.0, 0.0])

solucion = eliminacion_gaussiana(A, b)
print("--- ELIMINACIÓN GAUSSIANA ---")
print(f"Solución: {solucion}")

#--- Salida
#--- ELIMINACIÓN GAUSSIANA ---
#Solución: [ 1. -2. -2.]