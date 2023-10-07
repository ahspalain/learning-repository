# Inicializa una lista de tareas vacía
lista_de_tareas = {}

def agregar_tarea():
    tarea = input("Ingrese la tarea: ")
    lista_de_tareas[len(lista_de_tareas) + 1] = {"tarea": tarea, "completada": False}
    print("Tarea agregada con éxito.")

def eliminar_tarea():
    if len(lista_de_tareas) == 0:
        print("La lista de tareas está vacía.")
    else:
        print("Lista de tareas:")
        for tarea_id, tarea in lista_de_tareas.items():
            print(f"{tarea_id}. {tarea['tarea']} (Completada: {tarea['completada']})")

        tarea_id = int(input("Ingrese el número de tarea que desea eliminar: "))
        if tarea_id in lista_de_tareas:
            del lista_de_tareas[tarea_id]
            print("Tarea eliminada con éxito.")
        else:
            print("Tarea no encontrada.")

def marcar_completada():
    if len(lista_de_tareas) == 0:
        print("La lista de tareas está vacía.")
    else:
        print("Lista de tareas:")
        for tarea_id, tarea in lista_de_tareas.items():
            print(f"{tarea_id}. {tarea['tarea']} (Completada: {tarea['completada']})")

        tarea_id = int(input("Ingrese el número de tarea que desea marcar como completada: "))
        if tarea_id in lista_de_tareas:
            lista_de_tareas[tarea_id]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Tarea no encontrada.")

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intente nuevamente.")

print("¡Gracias por usar la lista de tareas!")
