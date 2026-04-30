#include <iostream>
#include <iomanip>

int main() {
    // Dos números muy grandes y muy cercanos
    double x = 1234567890.1234567;
    double y = 1234567890.1234560;

    // El resultado esperado es 0.0000007
    double resultado = x - y;

    std::cout << std::setprecision(17);
    std::cout << "x = " << x << std::endl;
    std::cout << "y = " << y << std::endl;
    std::cout << "Resultado real: " << resultado << std::endl;

    return 0;
}

