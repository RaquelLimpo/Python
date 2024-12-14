import os
from metodosPropios import leerDatos, mostrarDatos, incrementarPrecipitaciones, almacenarPrecipitacionesFichero, pintaMenu


def main():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    nombre_fichero = os.path.join(ruta_actual, "precipitaciones.txt")
    lista_precipitaciones = []

    while True:
        opcion = pintaMenu()
        if opcion == 1:
            lista_precipitaciones = leerDatos(nombre_fichero)
        elif opcion == 2:
            mostrarDatos(lista_precipitaciones)
        elif opcion == 3:
            lista_precipitaciones = incrementarPrecipitaciones(lista_precipitaciones)
        elif opcion == 4:
            almacenarPrecipitacionesFichero(lista_precipitaciones)
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

