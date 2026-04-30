#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    // 1. El Problema: Error de redondeo en punto flotante
    double a = 0.1 + 0.1 + 0.1;
    double b = 0.3;

    std::cout << std::setprecision(17); // Mostrar toda la precisión
    std::cout << "Valor de a (0.1 * 3): " << a << std::endl;
    std::cout << "Valor de b:           " << b << std::endl;

    // 2. Comparación directa (FALLA)
    std::cout << "\n--- Comparación con '==' ---" << std::endl;
    if (a == b) {
        std::cout << "Resultado: Son iguales" << std::endl;
    } else {
        std::cout << "Resultado: SON DIFERENTES (Error esperado)" << std::endl;
    }

    // 3. La Solución: Uso de Épsilon
    double epsilon = 0.00001;

    std::cout << "\n--- Comparación con Épsilon (" << epsilon << ") ---" << std::endl;
    if (std::abs(a - b) < epsilon) {
        std::cout << "Resultado: Son iguales (dentro del margen de error)" << std::endl;
    } else {
        std::cout << "Resultado: Son diferentes" << std::endl;
    }

    return 0;
}

