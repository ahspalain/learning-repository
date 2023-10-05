def pagototal(pago_wo, impuesto):
    return pago_wo + pago_wo*(impuesto/100)

pago_wo = float(input("Introduce el pago sin impuesto: "))
impuesto = float(input("Introduce el impuesto sin porcentaje: "))

print(f"El pago total es el siguiente {pagototal(pago_wo, impuesto)}")