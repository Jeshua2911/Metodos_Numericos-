import numpy as np
# Evita errores si hay un cero en la diagonal
A = np.array([[0.0, 2.0, 1.0], [1.0, -2.0, -3.0], [5.0, -1.0, -2.0]])
b = np.array([4.0, 0.0, -3.0])
# Nota: np.linalg.solve usa una variante de eliminación gaussiana
print("Eliminación 2 (Pivoteo):", np.linalg.solve(A, b))

#Salida
#Eliminación 2 (Pivoteo): [-0.94117647  3.23529412 -2.47058824]