palabra = input("Escribe una palabra: ").upper()

if palabra == palabra[::-1]:
    print("Tú palabra es un palindromo")

else:
    print("no es un palindromo")


#reemplazador

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))