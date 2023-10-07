import random

def simulador_de_dados():
    return random.randint(1,6)

print(f'Bienvenido al simulador de dados')

while True: 
    print(f'Su número es {simulador_de_dados()} del simulador')
    still_playing = input("¿Desea seguir jugando? (Y/N) ").lower()
    if still_playing == "y":
        print(simulador_de_dados())
    
    else:
        print("Gracias por participar")
        break


