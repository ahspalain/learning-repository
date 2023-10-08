import random

def playgame():
    n_to_guess = random.randint(1,100)
    lifes = 5
    lower_limit = -10
    upper_limit = 10

    while lifes >0:
        try:
            user_guess = int(input("Indique el número correcto: "))
        except ValueError:
            print("Ha ingresado un valor invalido")
            continue
        
        between_n = n_to_guess - user_guess

        if lower_limit <= between_n <= upper_limit:
            lifes -= 1
            print(f"Usted está cerca, le quedan: {lifes} vidas restantes.")
        elif lower_limit*2 <= between_n <= upper_limit*2:
            lifes -= 1
            print(f"Usted está un poco lejos, le quedan: {lifes} vidas restantes.")
        elif n_to_guess != user_guess:
            lifes -= 1
            print(f"Siga intentando, le quedan: {lifes} vidas restantes.")
        elif n_to_guess == user_guess:
            print(f'El numero: {user_guess} es el correcto, ¡Lo lograste!')
            stil_playing = input("¿Desea seguir jugando? (S/N) ").lower()
            if stil_playing != "s":
                break
    
    if lifes == 0:
        print(f'El numero: {n_to_guess} era el correcto, a la siguiente lo lograrás')
        stil_playing = input("¿Desea seguir jugando? (S/N) ").lower()
        if stil_playing == "s":
            return playgame()

    print("Gracias por participar")

welcome = "." * 72 + "\nBienvenido, debes adivinar el número al azar, seleccionado del 1 al 100\n" + "." * 72
print(welcome)

playgame()

