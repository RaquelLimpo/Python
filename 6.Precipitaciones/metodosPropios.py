MAX_INCREMENTO = 200
MIN_INCREMENTO = 1

def leerDatos(nombre_fichero):

    try:
        with open(nombre_fichero, "r") as file:
            return [float(line.strip()) for line in file]
    except FileNotFoundError:
        print(f"El fichero {nombre_fichero} no existe.")
        return []
    except ValueError:
        print("Error al leer los datos del fichero. Asegúrate de que contiene solo números.")
        return []

def mostrarDatos(lista):

    if not lista:
        print("No hay datos cargados.")
    else:
        print("Datos de precipitaciones:")
        for i, valor in enumerate(lista, start=1):
            print(f"{i}. {valor:.2f}")

def incrementarPrecipitaciones(lista):

    if not lista:
        print("No hay datos cargados.")
        return lista

    while True:
        try:
            incremento = float(input(f"Introduce un valor para incrementar (entre {MIN_INCREMENTO} y {MAX_INCREMENTO}): "))
            if MIN_INCREMENTO <= incremento <= MAX_INCREMENTO:
                return [valor + incremento for valor in lista]
            else:
                print(f"El valor debe estar entre {MIN_INCREMENTO} y {MAX_INCREMENTO}.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")

def almacenarPrecipitacionesFichero(lista):

    if not lista:
        print("No hay datos cargados.")
        return

    nombre_fichero = input("Introduce el nombre del fichero donde guardar los datos (incluye .txt): ")
    try:
        with open(nombre_fichero, "w") as file:
            for valor in lista:
                file.write(f"{valor:.2f}\n")
        print(f"Datos guardados en el fichero {nombre_fichero}.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def pintaMenu():

    print("\nMenú:")
    print("1. Leer datos de precipitaciones")
    print("2. Mostrar datos")
    print("3. Incrementar precipitaciones")
    print("4. Guardar datos en un fichero")
    print("5. Salir")
    try:
        return int(input("Selecciona una opción: "))
    except ValueError:
        print("Entrada inválida. Introduce un número.")
        return 0
