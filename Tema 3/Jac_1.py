import numpy as np

def jacobi_tolerancia(A, b, tol=1e-5, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    x_prev = np.zeros(n)
    
    print(f"{'Iter':<5} | {'Error':<12} | {'Solución'}")
    
    for k in range(max_iter):
        for i in range(n):
            suma = sum(A[i][j] * x_prev[j] for j in range(n) if i != j)
            x[i] = (b[i] - suma) / A[i][i]
        
        error = np.linalg.norm(x - x_prev, np.inf)
        print(f"{k+1:<5} | {error:<12.6f} | {x}")
        
        if error < tol:
            print(f"Convergencia alcanzada en {k+1} iteraciones.")
            return x
        x_prev = x.copy()
    return x

A = np.array([[4, -1, 1], [4, -8, 1], [-2, 1, 5]], dtype=float)
b = np.array([7, -21, 15], dtype=float)
jacobi_tolerancia(A, b)

#Salida
#Iter  | Error        | Solución
#1     | 3.000000     | [1.75  2.625 3.   ]
#2     | 1.250000     | [1.65625 3.875   3.175  ]
#3     | 0.287500     | [1.925  3.85   2.8875]
#4     | 0.112500     | [1.990625  3.9484375 3.       ]
#5     | 0.046875     | [1.98710937 3.9953125  3.0065625 ]
#6     | 0.010781     | [1.9971875  3.994375   2.99578125]
#7     | 0.004219     | [1.99964844 3.99806641 3.        ]
#8     | 0.001758     | [1.9995166  3.99982422 3.00024609]
#9     | 0.000404     | [1.99989453 3.99978906 2.9998418 ]
#10    | 0.000158     | [1.99998682 3.99992749 3.        ]
#11    | 0.000066     | [1.99998187 3.99999341 3.00000923]
#12    | 0.000015     | [1.99999604 3.99999209 2.99999407]
#13    | 0.000006     | [1.99999951 3.99999728 3.        ]
#Convergencia alcanzada en 13 iteraciones.