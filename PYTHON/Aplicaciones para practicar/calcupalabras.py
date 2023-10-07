def word_counter(words):
    # Dividir la cadena en palabras usando el espacio como separador
    word_list = words.split()
    # Contar el número de palabras en la lista
    word_count = len(word_list)
    return word_count

input_text = input("Ingrese el texto a contar:")
count = word_counter(input_text)
print(f'Hay {count} palabras en "{input_text}"')  # Esto imprimirá 3, que es el número de palabras en la cadena.
