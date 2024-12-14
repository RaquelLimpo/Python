#importamos turtle para que dibuje el circulo
import turtle

def dibujar_circulo(radio):
    pantalla = turtle.Screen()
    pantalla.title("Círculo en Python")
    tortuga = turtle.Turtle()
    tortuga.circle(radio)
    pantalla.mainloop()

# Programa principal
radio = float(input("Introduce el radio del círculo: "))
if radio > 0:
    dibujar_circulo(radio)
else:
    print("Eso no es posible! El radio debe ser mayor a 0!")