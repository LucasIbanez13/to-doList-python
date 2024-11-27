tareas = []

def mostrar_menu():
    print("\n--- To-Do List ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Listar tareas")
    print("4. Salir")

def agregar_tarea():
    tarea = input("Ingresa la tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea():
    try:
        listar_tareas()
        indice = int(input("Ingresa el número de la tarea que deseas eliminar: "))
        if 0 <= indice < len(tareas):
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("Índice fuera de rango.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def listar_tareas():
    if tareas:
        print("\n--- Tareas ---")
        for i, tarea in enumerate(tareas):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista.")

def ejecutar_todo_list():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            eliminar_tarea()
        elif opcion == "3":
            listar_tareas()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

ejecutar_todo_list()
