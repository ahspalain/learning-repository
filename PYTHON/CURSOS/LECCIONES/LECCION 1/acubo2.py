class Cubo:

    """Calculadora de Volumen de Cubo y Prisma Rectangular"""

    def __init__(self, lado1, lado2, lado3) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def volumen_cubo(self):
        return self.lado1 ** 3
    
    def volumen_prisma_rectangular(self):
        return self.lado1 * self.lado2 * self.lado3

def obtener_float_input(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingrese un número válido.")

while True:
    opcion_calculo = input("¿Desea calcular un cubo o un prisma rectangular (C/P): ").upper()
    
    if opcion_calculo == "C":
        lado = obtener_float_input("Ingrese la longitud del lado del cubo: ")
        cubo = Cubo(lado, lado, lado)
        print(f'El volumen del cubo es: {cubo.volumen_cubo()}')

    elif opcion_calculo == "P":
        lado1 = obtener_float_input("Ingrese el primer lado del prisma: ")
        lado2 = obtener_float_input("Ingrese el segundo lado del prisma: ")
        lado3 = obtener_float_input("Ingrese el tercer lado del prisma: ")
        prisma = Cubo(lado1, lado2, lado3)
        print(f'El volumen del prisma rectangular es: {prisma.volumen_prisma_rectangular()}')

    else:
        print("Ha ingresado un valor incorrecto")
    
    seguir_calculando = input("¿Desea continuar (Y/N): ").upper()
    if seguir_calculando != "Y":
        break

print("Gracias por su participación")
