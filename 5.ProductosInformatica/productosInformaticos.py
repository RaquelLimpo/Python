import os
from metodosPropios import listarCategorias, verificarEleccionCategoria, mostrarProductosCategoria

ruta_actual = os.path.dirname(os.path.abspath(__file__))
nombre_fichero = os.path.join(ruta_actual, "productosInformatica.txt")

productos = []
with open(nombre_fichero, 'r') as archivo:
    for linea in archivo:
        nombre, categoria, precio = linea.strip().split(',')
        productos.append({'nombre': nombre, 'categoria': categoria, 'precio': float(precio)})
categorias = list(set(producto['categoria'] for producto in productos))
listarCategorias(categorias)

indice_categoria = verificarEleccionCategoria(len(categorias))
categoria_seleccionada = categorias[indice_categoria]

productos_categoria = [
    producto for producto in productos if producto['categoria'] == categoria_seleccionada
]
mostrarProductosCategoria(productos_categoria)