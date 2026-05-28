def f_ideal(x): return np.sin(x)

def derivar_3_puntos(f, x, h):
    # CASO CON ERROR: h demasiado pequeño causa error de redondeo catastrófico
    return (f(x + h) - f(x - h)) / (2 * h)

# CASO DECIDIDO: Datos de telemetría de un dron (Posición a los tiempos 1s, 2s, 3s) -> h = 1.0s
# Evaluando la velocidad en el tiempo central t = 2s
tiempos_3p = np.array([1.0, 2.0, 3.0])
posiciones_3p = np.array([5.0, 12.0, 24.0]) # metros

def derivar_3_puntos_discreto(y, h):
    return (y[2] - y[0]) / (2 * h)

# Ejecuciones
print(f"3 Puntos Ideal (Derivada de sin(pi/4)): {derivar_3_puntos(f_ideal, np.pi/4, 0.01):.4f}")
print(f"3 Puntos con Error (h ridículamente bajo): {derivar_3_puntos(f_ideal, np.pi/4, 1e-16)}")
print(f"3 Puntos Decidido (Velocidad dron en t=2s): {derivar_3_puntos_discreto(posiciones_3p, 1.0):.4f} m/s")