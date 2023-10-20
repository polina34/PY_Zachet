from complex import Complex
from calculator import Calculator

complex1 = Complex(2, 3)
complex2 = Complex(-1, 4)

calculator = Calculator()

calculator.add(complex1, complex2)
print(calculator.result)  # Выход: 1+7i

calculator.subtract(complex1, complex2)
print(calculator.result)  # Выход: 3-1i

calculator.multiply(complex1, complex2)
print(calculator.result)  # Выход: -14+5i

calculator.divide(complex1, complex2)
print(calculator.result)  # Выход: -0.08-0.64i