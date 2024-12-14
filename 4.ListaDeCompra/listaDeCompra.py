from metodosPropios import agregar_producto, eliminar_producto, mostrar_lista

def menu():

    lista_compras = []

    while True:
        print("\n--- Menú Lista de Compras ---")
        print("1. Escribe el nombre del producto que quieres comprar")
        print("2. Borra el producto de la lista")
        print("3. Ver lista")
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido si quieres ir a comprar o escribe 4 para salir.")
            continue

        if opcion == 1:
            producto = input("Que quieres comprar?' Escribe el producto: ").strip()
            try:
                cantidad = int(input("Cuantos necesitas?: "))
                if cantidad > 0:
                    agregar_producto(lista_compras, producto, cantidad)
                else:
                    print("La cantidad debe ser mayor que 0.")
            except ValueError:
                print("Alguien no quiere ir a comprar. Introduce una cantidad válida.")
        elif opcion == 2:
            mostrar_lista(lista_compras)
            try:
                indice = int(input("Introduce el número del producto a eliminar: "))
                eliminar_producto(lista_compras, indice)
            except ValueError:
                print("Introduce un número válido.")
        elif opcion == 3:
            mostrar_lista(lista_compras)
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige entre 1 y 4.")

if __name__ == "__main__":
    menu()
