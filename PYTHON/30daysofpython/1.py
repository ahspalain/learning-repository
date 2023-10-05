def euclidian_distance(a, b, c, d):
    distancia = (a-c)**2 + (b-d)**2
    return distancia

a = float(input("Introduce la primera abcisa: "))
b = float(input("Introduce la primera ordenada: "))
c = float(input("Introduce la segunda abcisa: "))
d = float(input("Introduce la segunda ordenada: "))

resultado = euclidian_distance(a, b, c, d)
print(resultado)