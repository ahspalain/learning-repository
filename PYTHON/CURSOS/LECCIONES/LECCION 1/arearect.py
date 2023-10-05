class arectangulo:
    
    """Para calcular el área del rectangulo"""

    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
base = float(input("Ingrese el valor númerico de la base: "))
altura = float(input("Ingrese el valor númerico de la altura: "))

rectangulo1 = arectangulo(base, altura)
print(f'El área del rectangulo es: {rectangulo1.area()}')