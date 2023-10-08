import random

def play_game():
    list_values = [1, 2, 3]
    list_elements = ["tijera", "papel", "piedra"]

    eleccion_cpu = random.choice(list_elements)

    while True:
        try:
            eleccion_user = int(input("¿Cuál es tu elección? "))
            if eleccion_user in list_values:
                break
            else:
                print("Has seleccionado un valor erróneo. Debes elegir entre 1, 2 o 3.")
        except ValueError:
            eleccion_user = input("Has ingresado un valor inválido. ¿Deseas seguir jugando? (S/N) ").lower()
            if eleccion_user == "n":
                return False

    if list_elements[eleccion_user - 1] == eleccion_cpu:
        print(f"Tú has escogido {list_elements[eleccion_user - 1]} y tu contrincante {eleccion_cpu}, es un empate")
    elif (list_elements[eleccion_user - 1] == "tijera" and eleccion_cpu == "papel") or \
         (list_elements[eleccion_user - 1] == "papel" and eleccion_cpu == "piedra") or \
         (list_elements[eleccion_user - 1] == "piedra" and eleccion_cpu == "tijera"):
        print(f"Tú has escogido {list_elements[eleccion_user - 1]} y tu contrincante {eleccion_cpu}, tú ganas")
    else:
        print(f"Tú has escogido {list_elements[eleccion_user - 1]} y tu contrincante {eleccion_cpu}, has perdido")

    while True:
        still_playing = input("¿Deseas seguir jugando? (S/N) ").lower()
        if still_playing == "s":
            return True
        elif still_playing == "n":
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 'S' para seguir jugando o 'N' para salir.")

welcome = "." * 72 + "\nBienvenido, al juego del Piedra, Papel y Tijera.\nSelecciona uno de los elementos:\n#1 Tijera\n#2 Papel\n#3 Piedra\n" + "." * 72
print(welcome)

while play_game():
    pass

print("Gracias por participar")






# User
# import random

# def play_game():
#     list_values = [1,2,3]
#     list_elements = ["tijera","papel","piedra"]

#     eleccion_cpu = random.choice(list_elements)

#     try:
#         eleccion_user = int(input("¿Cuál es tu elección? "))
#         if eleccion_user in list_values:
#             print("Elección válida.")
#         else:
#             print("Has seleccionado un valor erróneo. Debes elegir entre 1, 2 o 3.")
#     except ValueError:
#         print("Has ingresado un valor inválido. Debes ingresar un número.")

#     while True:
#         if list_elements[eleccion_user-1] == eleccion_cpu:
#             print(f"Tú has escogido {list_elements[eleccion_user-1]} y tu contrincante {eleccion_cpu}, es un empate")
#             return play_game()
#         elif eleccion_cpu != list_elements[eleccion_user-1]:
#             if list_elements[eleccion_user-1] == "tijera" and eleccion_cpu == "papel":
#                 print(f"Tú has escogido {list_elements[eleccion_user-1]} y tu contrincante {eleccion_cpu}, tú ganas")
#                 return play_game()
#             elif list_elements[eleccion_user-1] == "papel" and eleccion_cpu == "piedra":
#                 print(f"Tú has escogido {list_elements[eleccion_user-1]} y tu contrincante {eleccion_cpu}, tú ganas")
#                 return play_game()
#             elif list_elements[eleccion_user-1] == "piedra" and eleccion_cpu == "tijera":
#                 print(f"Tú has escogido {list_elements[eleccion_user-1]} y tu contrincante {eleccion_cpu}, tú ganas")
#                 return play_game()
#             else:
#                 print(f"Tú has escogido {list_elements[eleccion_user-1]} y tu contrincante {eleccion_cpu}, has perdido")
#                 stillplaying = input("¿Deseas seguir jugando? (S/N) ").lower()
#                 if stillplaying != "s":
#                     break
#                 else:
#                     play_game()
#     print("Gracias por participar")

# welcome = "." * 72 + "\nBienvenido, al juego del Piedra, Papel y Tijera.\nSelecciona uno de los elementos:\n#1 Tijera\n#2 Papel\n#3 Piedra\n" + "." * 72
# print(welcome)
