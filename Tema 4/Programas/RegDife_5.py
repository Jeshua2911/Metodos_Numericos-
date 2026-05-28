def f_ideal(x): return np.exp(2 * x)

def derivar_5_puntos(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)

# CASO DECIDIDO / CON ERROR: Mapeo de datos discretos
# Supongamos que tenemos un arreglo de 5 lecturas de corriente eléctrica
corrientes = np.array([0.5, 0.8, 1.2, 1.7, 2.0]) # h = 0.5 segundos

def derivar_5_puntos_discreto(y, h, index):
    # CASO CON ERROR: Control de fronteras (Fuera de rango)
    if index < 2 or index > len(y) - 3:
        raise IndexError("¡Error! No hay suficientes puntos periféricos para aplicar 5 puntos.")
    return (-y[index+2] + 8*y[index+1] - 8*y[index-1] + y[index-2]) / (12 * h)

# Ejecuciones
print(f"5 Puntos Ideal (Derivada exacta): {derivar_5_puntos(f_ideal, 1.0, 0.01):.4f}")
print(f"5 Puntos Decidido (Cambio de corriente en nodo central): {derivar_5_puntos_discreto(corrientes, 0.5, 2):.4f} A/s")

try:
    print(derivar_5_puntos_discreto(corrientes, 0.5, 0)) # Provocando el error de frontera
except IndexError as e:
    print(f"Captura de Error: {e}")