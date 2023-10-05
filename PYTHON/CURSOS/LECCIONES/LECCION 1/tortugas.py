import random

meta = 20
caracol1 = 0
caracol2 = 0

while caracol1 <20 and caracol2 <20:
    avance_caracol1 = random.randint(1,4)
    avance_caracol2 = random.randint(1,4)

    caracol1 += avance_caracol1
    caracol2 += avance_caracol2

    print(f'El caracol1 avanza {avance_caracol1}, para un total de {caracol1}')
    print(f'El caracol1 avanza {avance_caracol2}, para un total de {caracol2}')
    print("--------------------------------")

if caracol1 < caracol2:
    print("El caracol 2 es el vencedor.")
elif caracol1 > caracol2:
    print("El caracol 1 es el vencedor.")
else:
    print("Esto es un empate.")