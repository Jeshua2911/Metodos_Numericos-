#include <iostream>
#include <limits>

int main() {
    int max = std::numeric_limits<int>::max(); // 2,147,483,647
    int resultado = max + 1; // Desbordamiento

    std::cout << "Maximo int: " << max << std::endl;
    std::cout << "Maximo + 1: " << resultado << std::endl;

    // Detección manual del desbordamiento (estilo didáctico)
    if (resultado < max) {
        std::cout << "Error detectado: ¡Desbordamiento!" << std::endl;
    }

    return 0;
}

