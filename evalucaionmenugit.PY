lista_alumnos = []

def mostrar_menu():

    print("\n--- MENÚ PRINCIPAL ---")

    print("1. Agregar alumno")

    print("2. Mostrar todos los alumnos")

    print("3. Eliminar alumno por nombre")

    print("4. Cerrar")



while True:

    mostrar_menu()

    opcion = input("Selecciona una opción (1-4): ")



    if opcion == "1":

        nombre = input("Ingresa el nombre del alumno: ").strip()

        if nombre.isalpha():

            lista_alumnos.append(nombre)

            print(f"Alumno '{nombre}' agregado correctamente.")

        else:

            print("Error: El nombre debe contener solo letras sin espacios ni números.")

    

    elif opcion == "2":
        if lista_alumnos:

            print("\n--- Lista de Alumnos ---")

            for i, alumno in enumerate(lista_alumnos, start=1):

                print(f"{i}. {alumno}")

        else:

            print("No hay alumnos registrados.")

    

    elif opcion == "3":

        if not lista_alumnos:

            print("No hay alumnos para eliminar.")

        else:

            nombre_eliminar = input("Ingresa el nombre del alumno a eliminar: ").strip()

            if nombre_eliminar in lista_alumnos:

                lista_alumnos.remove(nombre_eliminar)

                print(f"Alumno '{nombre_eliminar}' eliminado correctamente.")

            else:

                print(f"No se encontró al alumno '{nombre_eliminar}'.")



    elif opcion == "4":

        print("Programa cerrado.")

        break



    else:

        print("Opción no válida. Intenta nuevamente.")