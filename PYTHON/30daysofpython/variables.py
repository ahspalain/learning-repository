"""Day 2: 30 Days of python programming"""

#level1

first_name = "Adrian"
last_name = "Bringas"
full_name = "Adrian Bringas"
country = "Perú"
city = "Lima"
edad = 24
year = 2023
is_married = False
pene, cabello, carro = "15cm", "negro", "ferrari"

#level2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(edad))
print(type(year))
print(type(is_married))

print(len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

#nivel 3

radio = float(input("Ingrese el radio de la circunferencia: "))
pi = 3.1416
area_of_circle = pi * (radio**2)
circum_of_circle = 2 * pi * radio

print(f'{area_of_circle:.2f} y {circum_of_circle:2f}')

first_name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
full_name = input("Ingrese su nombre completo: ")
country = input("Ingrese su país: ")
edad = int(input("Ingrese su edad: "))

print(first_name)
print(last_name)
print(full_name)
print(country)
print(edad)

help()