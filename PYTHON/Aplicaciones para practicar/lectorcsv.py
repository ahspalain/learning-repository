import csv

# Nombre del archivo CSV que deseas leer
nombre_archivo = "ejemplo.csv"

# Función para leer y mostrar el contenido del archivo CSV en formato tabular
def mostrar_contenido_csv(nombre_archivo):
    try:
        with open(nombre_archivo, newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            
            # Leer las filas del archivo CSV y mostrarlas en formato tabular
            for fila in lector_csv:
                print('\t'.join(fila))
    
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

# Llamar a la función para mostrar el contenido del archivo CSV
mostrar_contenido_csv(nombre_archivo)
