#include <iostream>
#include <iomanip>
#include <cmath>

int main() {
    int iteraciones = 1000000; // Un millón de sumas
    double incremento = 0.1;

    // 1. Acumulación usando 'double'
    double sumaDouble = 0.0;
    for (int i = 0; i < iteraciones; i++) {
        sumaDouble += incremento;
    }

    // Resultado esperado
    double esperado = iteraciones * incremento;

    std::cout << std::setprecision(17);
    std::cout << "--- Acumulación en Bucle (1,000,000 de iteraciones) ---" << std::endl;
    std::cout << "Resultado esperado: " << esperado << std::endl;
    std::cout << "Resultado double:   " << sumaDouble << std::endl;
    std::cout << "Diferencia (Error): " << (sumaDouble - esperado) << std::endl;

    // 3. Verificación del error
    if (sumaDouble != esperado) {
        std::cout << "\nNOTA: El error de 'double' es notable tras un millón de sumas." << std::endl;
    }

    return 0;
}

