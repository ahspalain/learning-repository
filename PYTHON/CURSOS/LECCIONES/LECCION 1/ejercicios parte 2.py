
nombre_usuario = input("¿Cuál es tu nombre? ")
num_veces = int(input("¿Cuántas veces quieres que se repita tu nombre? "))

print((nombre_usuario + "\n") * int(num_veces)) #opción 1

for _ in range(num_veces):
    print(nombre_usuario)   #opción 2