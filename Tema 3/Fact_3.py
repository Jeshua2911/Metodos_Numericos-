import numpy as np

def factorizacion_qr(A):
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    print("--- PROCESO DE ORTOGONALIZACIÓN QR ---")
    for j in range(m):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], A[:, j])
            v = v - R[i, j] * Q[:, i]
        
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    print("Matriz Q (Ortogonal):\n", Q)
    print("Matriz R (Triangular):\n", R)
    
    # Verificación: Q * R debe ser igual a A
    print("\nVerificación (Q * R):\n", np.dot(Q, R))
    return Q, R

A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=float)
factorizacion_qr(A)

#Salida
#Matriz Q (Ortogonal):
# [[ 0.85714286 -0.39428571 -0.33142857]
# [ 0.42857143  0.90285714  0.03428571]
# [-0.28571429  0.17142857 -0.94285714]]
#Matriz R (Triangular):
# [[ 14.  21. -14.]
# [  0. 175. -70.]
# [  0.   0.  35.]]

#Verificación (Q * R):
# [[ 12. -51.   4.]
# [  6. 167. -68.]
# [ -4.  24. -41.]]