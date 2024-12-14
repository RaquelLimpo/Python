def listarCategorias(categorias):
    print("Categorías disponibles:")
    for idx, categoria in enumerate(categorias, start=1):
        print(f"{idx}. {categoria}")

def verificarEleccionCategoria(cantidad_categorias):
    while True:
        try:
            seleccion = int(input("Selecciona el número de la categoría: "))
            if 1 <= seleccion <= cantidad_categorias:
                return seleccion - 1  
                print("Por favor, selecciona un número válido.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def mostrarProductosCategoria(productos):
    if productos:
        print("\nProductos en la categoría seleccionada:")
        total_precio = 0
        for producto in productos:
            print(f"- {producto['nombre']} ({producto['precio']}€)")
            total_precio += producto['precio']
        print(f"\nTotal de productos: {len(productos)}")
        print(f"Precio medio: {total_precio / len(productos):.2f}€")
    else:
        print("\nNo hay productos en esta categoría.")


    print("\nProductos en la categoría seleccionada:")
    total_precio = 0
    for producto in productos:
        print(f"- {producto['nombre']} ({producto['precio']}€)")
        total_precio += producto['precio']

    print(f"\nTotal de productos: {len(productos)}")
    print(f"Precio medio: {total_precio / len(productos):.2f}€")
