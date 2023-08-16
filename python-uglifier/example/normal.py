from math import sqrt

class Complex:
    def __init__(self, a: float, b: float = 0):
        self.a = a
        self.b = b
    def __str__(self) -> str:
        return f"{self.a} + {self.b}i"
    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)
    def abs(self) -> float:
        return sqrt(self.a**2 + self.b**2)
    
a = Complex(1)
b = Complex(2, 1)
print(a + b)