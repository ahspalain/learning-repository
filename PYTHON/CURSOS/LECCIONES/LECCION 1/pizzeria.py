tipo_pizza = input("¿Quiere una pizza vegetarina? (Y/N) ").lower()

ingredientes_pizza = ["Pimiento", "Tofu", "Peperoni", "Jamon", "Salmón"]

if tipo_pizza == "y":
    print(ingredientes_pizza[0:2])
    ingrediente_elegido = input("¿Qué ingrediente desea? ")
    if (ingrediente_elegido == ingredientes_pizza[0]) or (ingrediente_elegido == ingredientes_pizza[1]):
        print(f'''Usted ha elegido {ingrediente_elegido}
Su pizza es de tipo vegetariana y los ingredentes son: {ingrediente_elegido}, tomate y mozzarela.''')
    
    else:
        print("Ha elegido un ingrediente incorrecto")

else:
    print(ingredientes_pizza[3:])
    ingrediente_elegido = input("¿Qué ingrediente desea? ")
    if (ingrediente_elegido == ingredientes_pizza[3]) or (ingrediente_elegido == ingredientes_pizza[4]) or (ingrediente_elegido == ingredientes_pizza[5]):
        print(f'''Usted ha elegido {ingrediente_elegido}
Su pizza es de tipo vegetariana y los ingredentes son: {ingrediente_elegido}, tomate y mozzarela.''')
    
    else:
        print("Ha elegido un ingrediente incorrecto")


# # Lista de ingredientes para pizzas vegetarianas y no vegetarianas
# ingredientes_vegetarianos = ["Pimiento", "Tofu"]
# ingredientes_no_vegetarianos = ["Peperoni", "Jamon", "Salmón"]

# tipo_pizza = input("¿Quiere una pizza vegetariana? (Y/N) ").lower()

# if tipo_pizza == "y":
#     print(", ".join(ingredientes_vegetarianos))
# else:
#     print(", ".join(ingredientes_no_vegetarianos))

# ingrediente_elegido = input("¿Qué ingrediente desea? ")

# if tipo_pizza == "y" and ingrediente_elegido in ingredientes_vegetarianos:
#     print(f'''Usted ha elegido {ingrediente_elegido}.
# Su pizza es de tipo vegetariana y los ingredientes son: {ingrediente_elegido}, tomate y mozzarella.''')
# elif tipo_pizza != "y" and ingrediente_elegido in ingredientes_no_vegetarianos:
#     print(f'''Usted ha elegido {ingrediente_elegido}.
# Su pizza no es vegetariana y los ingredientes son: {ingrediente_elegido}, tomate y mozzarella.''')
# else:
#     print("Ha elegido un ingrediente incorrecto o ha seleccionado un tipo de pizza incorrecto.")



