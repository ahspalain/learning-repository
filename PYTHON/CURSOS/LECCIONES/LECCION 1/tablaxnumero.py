n = int(input("Ingrese la tabla que desee ver: "))

for i in range(1,13):
    tabla = (i) * n
    print(f'{i} x {n} = {tabla}')


#tabla bidimensional de multiplicación

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")