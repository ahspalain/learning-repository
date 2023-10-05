n = int(input("Introduce un número mayor que 2: "))

for i in range(2,n):
    if n % i == 0:
        break

if i == n:
    print(f'{n} es primo.')

else:
    print(f'{n} no es primo')
