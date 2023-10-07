import random

#Definimos los caracteres permitidos para la contraseña:

letras_permitidas = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"

#Generamos la función que nos cree una contraseña según la longitud de caracteres indicada
def secure_password(longitud):
    contraseña = "".join(random.choices(letras_permitidas,k=longitud))
    return contraseña

#Generamos un input de números enteros para la longitud de la contraseña

char_question = int(input("¿De cuántos caracteres debe ser tu contraseña?: "))
print(secure_password(char_question))
        