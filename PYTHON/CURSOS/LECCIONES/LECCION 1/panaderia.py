
panes_vendidos = int(input("¿Cuantos panes del día se han vendido? "))
panes_pasados_vendidos = int(input("¿Cuantos panes pasados se han vendido? "))

precio_pan = 3.49 * panes_vendidos
precio_pan_pasado = (0.4 * 3.49) * panes_pasados_vendidos

precio_total =  precio_pan + precio_pan_pasado

print(f'''
El precio de los {panes_vendidos} panes del día es: {precio_pan:.2f} soles
Y el precio de los {panes_pasados_vendidos} es: {precio_pan_pasado:.2f} soles
El precio de todos los panes vendidos es: {precio_total:.2f} soles
''')
