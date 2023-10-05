
cesta = []

while True:
    items_cesta = input("ingrese los items que irán en la cesta: ").lower()

    if items_cesta == "fin":
        break
    cesta.append(items_cesta)

print("los items de la cesta son: ")
for item in cesta:
    print(item)
    

