# CASO IDEAL
def f_ideal(x): return np.sin(x)

def simpson38(f, a, b, n):
    # CASO CON ERROR: Validación de n múltiplo de 3
    if n % 3 != 0:
        raise ValueError("¡Error! Para Simpson 3/8, 'n' debe ser múltiplo de 3.")
        
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 3 * f(x_i)
            
    return (3 * h / 8) * suma

# CASO DECIDIDO: Fuerza (N) medida cada 1.5 metros (n=6 intervalos)
fuerzas = np.array([0, 15, 30, 45, 40, 25, 0])
def simpson38_discreto(y, h):
    n = len(y) - 1
    suma = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 0:
            suma += 2 * y[i]
        else:
            suma += 3 * y[i]
    return (3 * h / 8) * suma

# Ejecuciones
print(f"Simpson 3/8 Ideal: {simpson38(f_ideal, 0, np.pi, 12):.4f}")
print(f"Simpson 3/8 Decidido (Trabajo calculado): {simpson38_discreto(fuerzas, 1.5):.4f} J")

try:
    print(simpson38(f_ideal, 0, np.pi, 10)) # Forzando el error
except ValueError as e:
    print(f"Captura de Error: {e}")