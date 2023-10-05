class Vehiculo:
    def __init__(self, color, ruedas) -> None:
        self.color = color
        self.ruedas = ruedas

    def __str__(self) -> str:
        return f'Color: {self.color}, Ruedas: {self.ruedas}'

class Coche(Vehiculo): #km/hora solo enteros
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self) -> str:
        return f'De velocidad {self.velocidad} km/h {super().__str__()}'

class Bicicleta(Vehiculo): 
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self) -> str:
        return f'De tipo: {self.tipo} {super().__str__()}'
    

vehiculo1 = Vehiculo("Negro", 4)
print(vehiculo1)

coche1 = Coche("Negro", 4, 150)
print(coche1)

bicicleta1 = Bicicleta("Negro", 4, "montañosa")
print(bicicleta1)