class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        return Complex(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __sub__(self, other):
        return Complex(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)

    def __mul__(self, other):
        return Complex(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                       self.real_part * other.imaginary_part + self.imaginary_part * other.real_part)

    def __truediv__(self, other):
        denominator = other.real_part ** 2 + other.imaginary_part ** 2
        return Complex((self.real_part * other.real_part + self.imaginary_part * other.imaginary_part) / denominator,
                       (self.imaginary_part * other.real_part - self.real_part * other.imaginary_part) / denominator)

    def __str__(self):
        if self.imaginary_part < 0:
            return f"{self.real_part}{self.imaginary_part}i"
        else:
            return f"{self.real_part}+{self.imaginary_part}i"