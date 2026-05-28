def gs_con_log(A, b, it=10):
    n = len(b)
    x = [0.0] * n  # Vector inicial de ceros
    
    # Abrimos el archivo para escribir los resultados paso a paso
    with open("resultado_gs.txt", "w") as f:
        f.write("==================================================\n")
        f.write("         LOG DE ITERACIONES GAUSS-SEIDEL          \n")
        f.write("==================================================\n\n")
        
        for k in range(it):
            for i in range(n):
                # Desglosamos la suma de forma estricta para asegurar el comportamiento Gauss-Seidel
                s = 0.0
                for j in range(n):
                    if i != j:
                        s += A[i][j] * x[j]
                
                # Actualización de la variable actual
                x[i] = (b[i] - s) / A[i][i]
            
            # Convertimos el vector x a una cadena bonita para guardar en el txt
            x_str = "[" + ", ".join(f"{val:.6f}" for val in x) + "]"
            f.write(f"Iteracion {k+1}: {x_str}\n")
            
        f.write("\n==================================================\n")
        f.write("Proceso finalizado con éxito.\n")
        
    print("--------------------------------------------------")
    print("¡Historial guardado exitosamente en 'resultado_gs.txt'!")
    print("--------------------------------------------------")
    return x

A = [
    [4.0, 1.0, 2.0], 
    [3.0, 5.0, 1.0], 
    [1.0, 1.0, 3.0]
]

# Vector de términos independientes (Faltaba definirlo en tu script)
b = [9.0, 14.0, 11.0]

# Mandamos a llamar a la función para que corra el programa
solucion_final = gs_con_log(A, b, it=10)

# Mostramos el resultado final también en la terminal para comodidad
print(f"Solución final en terminal: {solucion_final}")

#salida
#Solución final en terminal: [0.2954554780517733, 2.0454541724517727, 2.8863634498321513]