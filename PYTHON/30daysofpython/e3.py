#1

age = int(24)
height = 123.5
imaginario = 1j

#2

altura = int(input("Ingrese la altura del triangulo: "))
base = int(input("Ingresa base del triangulo: "))
area_triangulo = (base * altura)/2

print(f'El área del triangulo es: {area_triangulo}')

#3
a = 2
b = 2
c = 6
d = 10
pendiente = (a - c) / (b - d)
euclides = (a - c)**2 + (b - d)**2

print(f'La pendiente es: {pendiente:.2f} y la distancia de euclides es: {euclides:.2f}')

#4

x = int(input("Introduce el valor de x: "))
y = x**2 + 6*x + 9

print(f'La ecuación y cuando x toma el valor de {x} es: {y}')

print(not len("python") == len("dragon"))

print("jargon" in "I hope ths curse is not full o jargon")

print(not "on" in ("dragon" or "jargon"))

print(len("python"))
print(float(len("python")))
print(str(len("python")))

n = int(input("introduce un número:"))
if n % 2 == 0:
    print("Es par")

else:
    print("es impar")
    
if 7//3 == int(2.7):
    print("Es verdad")
else:
    print("es falso")
    
print(type(10) == type("10"))

if int(9.8) == 10:
    print(True)

else:
    print(False)
    
rows = 5
columns = 3

# Display the table
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if j == 1:
            print(i, end=' ')
        print(i ** j, end=' ')
    print()  # Move to the next row