#include <iostream>
#include <iomanip>
#include <limits>

int main() {
    double valorDouble = 3.14159e10; // Número muy grande
    int valorInt = static_cast<int>(valorDouble); // Casting explícito

    std::cout << std::setprecision(15);
    std::cout << "Valor Original: " << valorDouble << std::endl;
    std::cout << "Valor Truncado: " << valorInt << std::endl;

    return 0;
}

