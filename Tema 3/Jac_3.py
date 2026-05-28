import numpy as np
import matplotlib.pyplot as plt

def jacobi_graficado(A, b, it=20, tol=1e-5):
    n = len(b)
    x = np.zeros(n)
    errores = []
    
    # Extraemos la diagonal como un vector
    d = np.diag(A)
    
    # Creamos la matriz R (A pero con ceros en la diagonal)
    R = A - np.diag(d)
    
    print("-" * 50)
    print(f"{'Iter':<6}{'x aproximado':<30}{'Error (Norma)':<12}")
    print("-" * 50)
    
    for k in range(1, it + 1):
        # Fórmula de Jacobi vectorizada correctamente: (b - R*x) / d
        x_new = (b - np.dot(R, x)) / d
        
        # Calculamos la norma euclidiana del error entre iteraciones
        error = np.linalg.norm(x_new - x)
        errores.append(error)
        
        # Formateamos el vector x para imprimirlo bonito
        x_str = "[" + ", ".join(f"{val:.4f}" for val in x_new) + "]"
        print(f"{k:<6}{x_str:<30}{error:<12.5e}")
        
        # Guardamos la actualización
        x = x_new
        
        # Criterio de parada opcional por si converge antes de las 'it' iteraciones
        if error < tol:
            print("-" * 50)
            print(f"¡Convergencia alcanzada en la iteración {k}!")
            break


A = np.array([[5.0, -1.0, 1.0], 
              [2.0, 4.0, 0.0], 
              [1.0, 1.0, 5.0]])

b = np.array([10.0, 12.0, -1.0])

# Ejecutar el método
solucion = jacobi_graficado(A, b, it=15)

#salida
#-------------------------------------------------
#Iter  x aproximado                  Error (Norma)
#--------------------------------------------------
#1     [2.0000, 3.0000, -0.2000]     3.61109e+00 
#2     [2.6400, 2.0000, -1.2000]     1.55229e+00 
#3     [2.6400, 1.6800, -1.1280]     3.28000e-01 
#4     [2.5616, 1.6800, -1.0640]     1.01206e-01 
#5     [2.5488, 1.7192, -1.0483]     4.41174e-02 
#6     [2.5535, 1.7256, -1.0536]     9.53761e-03 
#7     [2.5558, 1.7232, -1.0558]     3.99008e-03 
#8     [2.5558, 1.7221, -1.0558]     1.16830e-03 
#9     [2.5556, 1.7221, -1.0556]     3.34797e-04 
#10    [2.5555, 1.7222, -1.0555]     1.33083e-04 
#11    [2.5555, 1.7222, -1.0555]     3.04844e-05 
#12    [2.5556, 1.7222, -1.0556]     1.27677e-05 
#13    [2.5556, 1.7222, -1.0556]     3.69693e-06 
#--------------------------------------------------
#¡Convergencia alcanzada en la iteración 13!