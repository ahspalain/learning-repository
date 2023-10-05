sexo = input("Ingrese su género(F/M): ").lower()
nombre = input("Ingrese su nombre: ").lower()

if (sexo == "f" and nombre < "m") or (sexo == "m" and nombre > "n"):
    print("Usted es del grupo A")

else:
    print("Usted es del grupo B")


renta_anual = int(input("Ingrese su renta anual: "))

if 0 < renta_anual < 10000:
    tipo_impositorio = 5

elif 10000 < renta_anual < 20000:
    tipo_impositorio = 15


elif 20000 < renta_anual < 35000:
    tipo_impositorio = 20


elif 35000 < renta_anual < 60000:
    tipo_impositorio = 30


else:
    tipo_impositorio = 45

print(f'Tu tipo impositoro es: {tipo_impositorio}% y debes pagar {renta_anual * (tipo_impositorio/100):.2f} euros.')

