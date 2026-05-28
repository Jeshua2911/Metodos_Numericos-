import numpy as np

# CASO IDEAL
def f_ideal(x): return x**2 + 2

# CASO CON ERROR (Singularidad cerca de 0)
def f_error(x): return 1 / (x + 1e-5) 

# CASO DECIDIDO (Simulación de datos de sensores de velocidad)
# Datos discretos: Tiempo (s) y Velocidad (m/s)
tiempo = np.array([0, 2, 4, 6, 8, 10])
velocidad = np.array([0, 5, 12, 18, 22, 25])

def trapecio_analitico(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        suma += 2 * f(a + i * h)
    return (h / 2) * suma

def trapecio_discreto(x, y):
    n = len(x) - 1
    suma = 0.0
    for i in range(n):
        h = x[i+1] - x[i]
        suma += (h / 2) * (y[i] + y[i+1])
    return suma

# Ejecuciones
print(f"Trapecio Ideal: {trapecio_analitico(f_ideal, 0, 2, 100):.4f}")
print(f"Trapecio con Error (Inestabilidad): {trapecio_analitico(f_error, 0, 2, 100):.4f}")
print(f"Trapecio Decidido (Distancia recorrida): {trapecio_discreto(tiempo, velocidad):.4f} metros")