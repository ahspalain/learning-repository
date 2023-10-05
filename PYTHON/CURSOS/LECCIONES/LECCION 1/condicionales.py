#ejercicio1

num_a = int(input("ingrese el primer numero: "))
num_b = int(input("ingrese el segundo numero: "))

if num_b < 0 > num_b:
    # div_A_B = num_a / num_b
    print(f'El resultado es: {num_a/num_b:.2f}')

else:
    print("El divisor es incorrecto")

num_c = int(input("ingrese el tecer numero: "))

if num_c % 2 == 0:
    print("Es par.")

else:
    print("Es impar")

#ejercicio 2

edad = int(input("Ingrese su edad: "))
salario = int(input("Ingrese su salario mensual: "))

if edad > 16 and salario > 1000:
    print("Usted debe tributar")

else:
    print("Usted no es apto para tributar")