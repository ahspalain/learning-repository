class Aritmetica:

    """
    Clase Aritmetica para realizar sumas, restas, multiplicación, etc
    """

    def  __init__(self, operandoA, operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    
    def potenciar(self):
        return self.operandoA ** self.operandoB
    
    
aritmetica1 = Aritmetica(5,3)
print(aritmetica1.sumar())

aritmetica2 = Aritmetica(5,3)
print(aritmetica1.restar())

aritmetica3 = Aritmetica(5,3)
print(aritmetica1.multiplicar())

aritmetica4 = Aritmetica(5,3)
print(aritmetica1.dividir())

aritmetica5 = Aritmetica(5,3)
print(aritmetica1.potenciar())
