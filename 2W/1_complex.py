class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


# --- Test ---
a = ComplexNumber(3, 2)
b = ComplexNumber(1, 7)

print("a =", a)
print("b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
