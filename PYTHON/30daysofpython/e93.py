def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return f'{number} no es primo.'
    return f'{number} es primo'

print(is_prime(21))
        
def is_unique(*args):
    list_args = list(args)
    numeros_repetidos = []
    for arg in args:
        frecuencia = list_args.count(arg)
        if frecuencia > 1:
            numeros_repetidos.append(arg)
            return f' La lista no tiene items únicos, puedes verlos aquí: {numeros_repetidos}'
        else:
            return f'La lista es única'
        
print(is_unique(1,2,3))

def is_number(*data):
    list_data = list(data)
    for elementos in list_data:
        if not isinstance(elementos,(int, float)):
            return f'Los elementos no son de tipo númerico'
    return f'Los elementos introducidos no son de tipo númerico'

print(is_number(1,2,3,"hola",4))
        
def can_be_variable(*vwords):
    words_cant_be_variables = []

    for word in vwords:
        if not str(word).isidentifier():
            words_cant_be_variables.append(word)
    
    if words_cant_be_variables:
        return f'Estos valores {words_cant_be_variables} no pueden ser variables, por lo tanto no todos los valores pueden ser variables'
    
    return f'Todos los valores pueden ser variables'

print(can_be_variable(1,1,1,1,1))




 




