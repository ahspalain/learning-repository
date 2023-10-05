capital_invertir = float(input("Introduce el capital a invertir: "))
interes_anual = float(input("Ingresa el porcentaje en decimales del interes anual: "))
años = int(input("Ingrese los años a invertir: "))



for i in range(años): # i es el que recorre el rango.
    inversión = capital_invertir * ((1+interes_anual)**años)
    print(f'Tu inversión en {i+1} es: {inversión:.2f} soles.')
