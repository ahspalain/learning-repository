import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "computadora", "juego", "desarrollo", "inteligencia"]

# Selecciona una palabra al azar de la lista
palabra_oculta = random.choice(palabras)

# Inicializa las variables
intentos_maximos = 6
intentos = 0
letras_adivinadas = []

# Función para mostrar la palabra oculta con las letras adivinadas
def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Comienza el juego
print("¡Bienvenido al juego del ahorcado!")
print(f"Adivina la palabra: {mostrar_palabra_oculta(palabra_oculta, letras_adivinadas)}")

while True:
    # Solicita al jugador una letra o la palabra completa
    adivinanza = input("Ingresa una letra o adivina la palabra completa: ").lower()

    # Incrementa el número de intentos
    intentos += 1

    # Verifica si la adivinanza es una letra válida
    if len(adivinanza) == 1 and adivinanza.isalpha():
        # Verifica si la letra ya se adivinó
        if adivinanza in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra.")
        elif adivinanza in palabra_oculta:
            letras_adivinadas.append(adivinanza)
            print(f"¡Correcto! {adivinanza} está en la palabra.")
        else:
            print(f"Incorrecto. {adivinanza} no está en la palabra.")
    elif adivinanza == palabra_oculta:
        print(f"¡Correcto! La palabra era '{palabra_oculta}'.")
        break
    else:
        print("Entrada no válida. Intenta nuevamente.")

    # Muestra la palabra oculta con las letras adivinadas
    print(f"Palabra: {mostrar_palabra_oculta(palabra_oculta, letras_adivinadas)}")

    # Verifica si el jugador ganó o perdió
    if mostrar_palabra_oculta(palabra_oculta, letras_adivinadas) == palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra correctamente.")
        break
    elif intentos >= intentos_maximos:
        print("¡Oh no! Has agotado todos tus intentos. La palabra era:", palabra_oculta)
        break
