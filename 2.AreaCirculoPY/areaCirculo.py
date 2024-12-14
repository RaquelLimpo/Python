#Escribe un programa que solicite al usuario el radio de un círculo. A continuación, el programa deberá calcular y 
# mostrar el área del círculo. El valor introducido debe considerarse con decimales y el resultado debe expresarse con dos decimales.

import math

def calculoArea(radio):
    # Calcula el área del círculo utilizando la fórmula: Área = π * radio^2
    return math.pi * (radio ** 2)

def main():
    try:
        radio = float(input("Escribe el radio del círculo que quieres saber (debe ser mayor a 0): "))
        if radio <= 0:
            print("Error: El radio debe ser un número mayor a 0.")
        else:
            area = calculoArea(radio)
            print(f"El área del círculo con radio {radio:.2f} es: {area:.2f}")
    except ValueError:
        print("Eso no es posible! El radio debe ser mayor a 0!")

if __name__ == "__main__":
    main()