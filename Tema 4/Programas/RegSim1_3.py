# CASO IDEAL
def f_ideal(x): return np.exp(x)

def simpson13(f, a, b, n):
    # CASO CON ERROR: Validación de n par
    if n % 2 != 0:
        raise ValueError("¡Error! Para Simpson 1/3, 'n' debe ser un número PAR.")
        
    h = (b - a) / n
    suma = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            suma += 2 * f(x_i)
        else:
            suma += 4 * f(x_i)
            
    return (h / 3) * suma

# CASO DECIDIDO: Áreas transversales de un tanque cada 2 metros
areas_tanque = np.array([4.0, 5.5, 6.2, 5.0, 3.8]) # n=4 intervalos (par)
def simpson13_discreto(y, h):
    n = len(y) - 1
    suma = y[0] + y[-1]
    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * y[i]
        else:
            suma += 4 * y[i]
    return (h / 3) * suma

# Ejecuciones
print(f"Simpson 1/3 Ideal: {simpson13(f_ideal, 0, 1, 10):.4f}")
print(f"Simpson 1/3 Decidido (Volumen tanque): {simpson13_discreto(areas_tanque, 2.0):.4f} m³")

try:
    print(simpson13(f_ideal, 0, 1, 11)) # Forzando el error
except ValueError as e:
    print(f"Captura de Error: {e}")