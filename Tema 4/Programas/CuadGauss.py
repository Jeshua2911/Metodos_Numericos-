# CASO IDEAL (Polinomio de grado 3)
def f_ideal(x): return x**3 - 2*x + 5

# CASO CON ERROR (Función con valor absoluto / pico no derivable)
def f_error(x): return np.abs(x - 1)

def cuadratura_gaussiana_2p(f, a, b):
    # Nodos y pesos estándar
    t1, t2 = -1 / np.sqrt(3), 1 / np.sqrt(3)
    w1, w2 = 1.0, 1.0
    
    # Cambio de variable
    x1 = ((b - a) / 2) * t1 + ((a + b) / 2)
    x2 = ((b - a) / 2) * t2 + ((a + b) / 2)
    
    # Integral
    integral = ((b - a) / 2) * (w1 * f(x1) + w2 * f(x2))
    return int(integral) if np.isclose(integral, round(integral)) else float(integral)

# CASO DECIDIDO: Aproximación de la distribución Normal Integrada (0 a 1)
def f_normal(x): return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Ejecuciones
print(f"Gauss Ideal (Exacto matemático): {cuadratura_gaussiana_2p(f_ideal, 0, 2)}")
print(f"Gauss con Error debido al pico: {cuadratura_gaussiana_2p(f_error, 0, 2):.4f} (Real debería ser 1.0)")
print(f"Gauss Decidido (Probabilidad campana de Gauss): {cuadratura_gaussiana_2p(f_normal, 0, 1):.4f}")