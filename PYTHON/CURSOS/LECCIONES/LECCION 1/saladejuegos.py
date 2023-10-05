edad = int(input("Ingrese su edad:"))

if  0 <= edad < 4:
    pago = ""

elif 4 <= edad < 18:
    pago = 5

elif edad >= 18:
    pago = 10

if pago == "":
    print("El ingreso es gratis.")

else:
    print(f'El pago es de {pago} soles para ingresar.')


# edad = int(input("Ingrese su edad:"))

# # Definir las tarifas como variables
# tarifa_gratis = ""
# tarifa_nino = 5
# tarifa_adulto = 10

# if 0 <= edad < 4:
#     pago = tarifa_gratis
# elif 4 < edad < 18:
#     pago = tarifa_nino
# elif edad >= 18:
#     pago = tarifa_adulto

# if pago == "":
#     print("El ingreso es gratis.")
# else:
#     print(f'El pago es de {pago} soles para ingresar.')

