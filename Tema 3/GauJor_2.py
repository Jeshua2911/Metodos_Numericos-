import numpy as np

def resolver_gauss_jordan(matriz):
    n = len(matriz)
    for i in range(n):
        # Convertir el pivote en 1
        pivote = matriz[i][i]
        matriz[i] = matriz[i] / pivote
        
        # Hacer ceros en los demás renglones
        for j in range(n):
            if i != j:
                factor = matriz[j][i]
                matriz[j] = matriz[j] - factor * matriz[i]
    return matriz

# Sistema 3x3:
# x + y + z = 6
# 2y + 5z = -4
# 2x + 5y - z = 27
sistema = np.array([[1.0, 1.0, 1.0, 6.0],
                    [0.0, 2.0, 5.0, -4.0],
                    [2.0, 5.0, -1.0, 27.0]])

print("--- EJERCICIO 2: SISTEMA 3X3 ---")
resultado = resolver_gauss_jordan(sistema)
print(resultado)
print("\nSoluciones: x={}, y={}, z={}".format(*resultado[:, -1]))


#Salida


#[[ 1.  0.  0.  5.]
 #[ 0.  1.  0.  3.]
 #[-0. -0.  1. -2.]]

#Soluciones: x=5.0, y=3.0, z=-2.0