
deposito = float(input("Introduce la cantidad a depositar para abrir tu cuenta bancaria:"))
interes = 0.04
años = 1

while True:
    balance = deposito*(interes + 1)**años
    print(f'Tu saldo final {balance:.2f} en el año {años}')
    años += 1

    if años == 4:
        break

print("Gracias por su participación")