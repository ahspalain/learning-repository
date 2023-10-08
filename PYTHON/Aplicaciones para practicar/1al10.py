for i in range(1,11):
    print(i)

nombres = ["Adrian", "David", "Ariel", "Andre", "Jeanpierre", "Jesus", "Ricardo", "Brihana", "Fernando", "Alfonso"]

for i in nombres:
    print(i)

# Definir una lista de números
lista_numeros = [12, 45, 67, 23, 9, 56, 72, 34]

# Inicializar una variable para almacenar el número más grande, asumiendo que el primer número es el más grande
numero_mas_grande = lista_numeros[0]

# Utilizar un ciclo for para recorrer la lista
for numero in lista_numeros:
    # Comprobar si el número actual es mayor que el número más grande
    if numero > numero_mas_grande:
        # Si es mayor, actualizar el número más grande
        numero_mas_grande = numero

# Al final del ciclo, la variable numero_mas_grande contendrá el número más grande en la lista
print("El número más grande en la lista es:", numero_mas_grande)


numero_para_tabla = int(input("Ingrese el número de la tabla que desea: "))

for i in range(13):
    multiplicacion = i * numero_para_tabla
    print(f'{i} x {numero_para_tabla} = {multiplicacion}')


number = int(input("Ingrese desde donde comience la cuenta regresiva: "))

while True:
    if number > 0:
        print(number)
        number -= 1
    elif number == 0:
        print(number)
        print("Despliegue")
        break

while True:
    for i in range(2,21,2):
        print(i)
    break


suma = 0  # Inicializa la suma fuera del bucle

while True:
    numero1 = int(input("Ingrese su número a sumar: "))
    if numero1 >= 0:
        suma += numero1
        print("Suma parcial:", suma)
    elif numero1 < 0:
        print("Suma total:", suma)
        break
