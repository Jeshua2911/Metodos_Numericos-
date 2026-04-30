#include <iostream>
#include <iomanip>

int main() {
    // Un double tiene aproximadamente 15-17 dígitos significativos
    double numeroGrande = 1.0e16; // 1 seguido de 16 ceros
    double numeroPequeno = 1.0;

    double resultado = numeroGrande + numeroPequeno;

    std::cout << "--- Demostración de Pérdida de Precisión ---" << std::endl;
    std::cout << std::fixed << std::setprecision(0);
    std::cout << "Número Grande:   " << numeroGrande << std::endl;
    std::cout << "Número Pequeño:  " << numeroPequeno << std::endl;
    std::cout << "Suma Resultante: " << resultado << std::endl;

    // Verificación lógica
    if (resultado == numeroGrande) {
        std::cout << "\nRESULTADO: El número pequeño 'desapareció'." << std::endl;
        std::cout << "La suma es igual al número original debido a la falta de bits en la mantisa." << std::endl;
    }

    return 0;
}

