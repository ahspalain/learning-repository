import csv

# Función para calcular el promedio de una lista de números
def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    total = sum(calificaciones)
    return total / len(calificaciones)

# Nombre del archivo CSV que contiene las calificaciones
nombre_archivo = "calificaciones.csv"

# Leer el archivo CSV y calcular el promedio de calificaciones
try:
    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        
        for fila in lector_csv:
            nombre = fila["Nombre"]
            calificaciones = [int(fila["Calificacion1"]), int(fila["Calificacion2"]), int(fila["Calificacion3"])]
            promedio = calcular_promedio(calificaciones)
            print(f"Estudiante: {nombre}, Promedio de calificaciones: {promedio:.2f}")
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
    