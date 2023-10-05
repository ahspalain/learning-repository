class acubo:

    """Área de un cubo"""

    def __init__(self, lado1, lado2, lado3) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def volumenc(self):
        return self.lado1 ** 3
    
    def volumenp(self):
        return self.lado1 * self.lado2 * self.lado3
    
while True:
    qcalcu = input("¿Desea calcular un cubo o un prisma rectangular (C/P): ").upper()
    if qcalcu == "P":
        lado1 = float(input("Ingrese el primer lado: "))
        lado2 = float(input("Ingrese el segundo lado: "))
        lado3 = float(input("Ingrese el tercer lado: "))
        prisma1 = acubo(lado1, lado2, lado3)
        print(f'El volumen del prisma rectangular es: {prisma1.volumenp()}')

    elif qcalcu == "C":
        lado1 = float(input("Ingrese el primer lado: "))
        cubo1 = acubo(lado1, lado1, lado1)
        print(f'El volumen del cubo es: {cubo1.volumenc()}')
    
    else:
        print("Ha ingresado un valor incorrecto")
    
    scalc = input("¿Deseas continuar(Y/N): ").upper()
    if scalc != "Y":
        break
print("Gracias por su participación")





#lado = float(input("Ingresa la medida del lado del cubo: "))

#cubo1 = acubo(lado)
#print(f'El volumen del cubo es: {cubo1.volumenc():.2f}')

#property
#nombre.setter
