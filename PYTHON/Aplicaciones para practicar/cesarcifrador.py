letras_1 = "abcdefghijklmnñopqrstuvwxyz"

def cifrador_de_palabras(word, n):
    palabra_cifrada = ""
    for letra in word:
        if letra in letras_1:
            indice_original = letras_1.index(letra)
            indice_cifrado = (indice_original + n) % len(letras_1)
            letra_cifrada = letras_1[indice_cifrado]
            palabra_cifrada += letra_cifrada
        else:
            palabra_cifrada += letra  # Mantén los caracteres que no están en letras_1 sin cifrar
    return palabra_cifrada

palabra_a_cifrar = input("¿Qué palabra quieres cifrar en el metodo de Cesar? ")
avance_cifrado = int(input('¿Cuántos caracteres quieres que avance el cifrado? '))

print(cifrador_de_palabras(palabra_a_cifrar, avance_cifrado))
