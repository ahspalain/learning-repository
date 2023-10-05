def calcelsius(farenheit):
    return (farenheit - 32)*(5/9)

def calfarenheit(celsius):
    return celsius * 1.8 + 32

while True:
    qcalcu = input("Coloque la inicial de la temperatura (C ó F) que desee calcular: ")
    if qcalcu == "C":
        farenheit = float(input("Ingrese la temperatura en °F: "))
        print(f'Su temperatura ° {farenheit} F en Celsius es ° {calcelsius(farenheit):.2f}')
    elif qcalcu == "F":
        celsius = float(input("Ingrese la temperatura en °C: "))
        print(f'Su temperatura ° {celsius} C en Farenheit es ° {calfarenheit(celsius):.2f}')
    else:
        print("Ingreso un valor incorrecto")

    scalc = input("¿Deseas continuar(Y/N): ")
    if scalc.upper() == "N":
        break
print("Gracias por su participación")





