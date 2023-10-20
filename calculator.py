
class Calculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.result = None
        return cls._instance

    def add(self, complex_num1, complex_num2):
        self.result = complex_num1 + complex_num2

    def subtract(self, complex_num1, complex_num2):
        self.result = complex_num1 - complex_num2

    def multiply(self, complex_num1, complex_num2):
        self.result = complex_num1 * complex_num2

    def divide(self, complex_num1, complex_num2):
        self.result = complex_num1 / complex_num2
