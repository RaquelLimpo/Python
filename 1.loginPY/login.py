#Escribe un programa que solicite al usuario  ingresar un nombre de usuario y una contraseña. 
# El usuario tendrá inicialmente 3 intentos para acceder al sistema.

import os

def limpiar_pantalla():
    """Limpia la pantalla dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def login():
    intentos = 3

    while intentos > 0:
        limpiar_pantalla()
        print(f"Tienes {intentos} intento(s) restante(s).\n")

        usuario = input("Ingrese el nombre de usuario: ").strip()
        contrasena = input("Ingrese la contraseña: ").strip()

        if usuario == "admin" and contrasena == "admin123":
            print("\nHas accedido al sistema como Admin.")
            return
        elif usuario == "dporti" and contrasena == "1234":
            print("\nBienvenido al sistema, David Porti.")
            return
        elif usuario == "guest" and contrasena == "guestpass":
            print("\nBienvenido al sistema en modo invitado.")
            return
        elif usuario == "newuser" and contrasena == "newpass":
            print("\nCuenta creada correctamente para Nuevo Usuario.")
            return
        else:
            intentos -= 1
            print(f"\nNo es posible acceder con las credenciales proporcionadas. Intentos restantes: {intentos}")

    limpiar_pantalla()
    print("\nPrograma bloqueado.")

if __name__ == "__main__":
    login()
