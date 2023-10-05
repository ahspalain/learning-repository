email = input("Introduce tu correo electrónico: ")
print(email[:email.find("@")] + "@ceu.es")


# email[:email.find("@")]: Descompone la dirección de correo electrónico ingresada por el usuario. La función email.find("@") busca la posición del símbolo "@" en la dirección de correo electrónico y devuelve su índice. Luego, se utiliza esta posición para obtener una subcadena de email desde el principio hasta justo antes del símbolo "@".

# + "@ceu.es": Agrega la cadena "@ceu.es" al final de la subcadena obtenida en el paso anterior. Esto modifica la dirección de correo electrónico original y la convierte en una dirección que termina en "@ceu.es".

# Finalmente, el resultado se imprime en la pantalla utilizando la función print(). El resultado es la dirección de correo electrónico modificada, que consiste en la parte original antes de "@" seguida de "@ceu.es".