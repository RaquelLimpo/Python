def agregar_producto(lista_compras, producto, cantidad):

    for item in lista_compras:
        if item["producto"].lower() == producto.lower():
            print(f"El producto '{producto}' ya está en la lista de compras. Debe apetecerte mucho")
            return
    lista_compras.append({"producto": producto, "cantidad": cantidad})
    print(f"'{producto}' añadido correctamente. Necesitas {cantidad}.")

def eliminar_producto(lista_compras, indice):
    try:
        producto_eliminado = lista_compras.pop(indice - 1)
        print(f"'{producto_eliminado['producto']}' ha sido eliminado de la lista. No se lo diremos a nadie")
    except IndexError:
        print("Índice inválido. Intenta nuevamente.")

def mostrar_lista(lista_compras):
    
    if not lista_compras:
        print("La lista de compras está vacía.")
        return
    print("Lista de compras:")
    for i, item in enumerate(lista_compras, start=1):
        print(f"{i}. {item['producto']} - Cantidad: {item['cantidad']}")
