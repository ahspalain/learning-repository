def media_cal(*args):
    media_sum = 0
    for arg in args:
        media_sum += arg
    return media_sum/len(args)

print(media_cal(1,2,3,4))

def mediana_cal(*args):
     arg_list = list(args)
     arg_list.sort()
     posicion_mitad = len(arg_list)//2
     if len(arg_list) % 2 == 0:
          mediana = arg_list[posicion_mitad-1]
          return mediana
     else:
          mediana = arg_list[posicion_mitad]
          return mediana

print(mediana_cal(1,3,2,5))


def rango_variacion(*args):
     args_list = list(args)
     args_list.sort()
     rango_v = args_list[-1] - args_list[0]
     return rango_v

print(rango_variacion(1,2,3,6,7,10,11,4))


def moda_nums(*args):
    args_list = list(args)
    max_frecuencia = 0
    moda = []

    for num in args_list:
        frecuencia = args_list.count(num)  # Cuenta cuántas veces aparece num en la lista
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            moda = [num]
        elif frecuencia == max_frecuencia and num not in moda:
            moda.append(num)
    return moda

print(moda_nums(1,1,1,1,1,2,3,3,3,3,1,3,3))

def varianza(*args2):
    sum_of_values = 0
    n = len(args2)
    for arg in args2:
        sum_of_values += arg
    
    media_values = sum_of_values/n
    diference_media_values = []

    for arg in args2:
         value_diference = (arg - media_values)**2
         diference_media_values.append(value_diference)
    
    suma_diferencias = float(sum(diference_media_values))
    varianza = suma_diferencias/(n-1)
    return varianza

resultado_varianza = varianza(20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26)
print(resultado_varianza)

def desviation_sd(varianza):
     desviacion = varianza ** 0.5
     return desviacion
print(desviation_sd(resultado_varianza))