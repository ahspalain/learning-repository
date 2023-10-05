
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mayusculas_xpalabra(palabras):
    return palabras.upper()
    
resultado = map(mayusculas_xpalabra,countries)
print(list(resultado))

def square_number(numb):
    return numb**2

resultado1 = map(square_number, numbers)
print(list(resultado1))

resultado2 = map(mayusculas_xpalabra,names)
print(list(resultado2))

