#(MasterMindPY) (1 punto): Escribe un programa que genere aleatoriamente un valor entero entre 1 y 20 para a continuación pedir al usuario que lo acierte 
# introduciendo el valor que crea que puede ser. 

import random

def juego_adivinar_numero():

    numero_secreto = random.randint(1, 20)
    intentos = 5 
    intentos_usados = 0

    print("¡Bienvenido al juego Ayuda a Medusin!")
    print("Medusin ha olvidado el pin de su ordenador y debes ayudarle a entrar.\nPara ello debes encontrar el codigo de 4 dígitos que lo desbloquea. ")
    print("Son numeros entre 1 y 20. Pero cuidado solo tienes 5 intentos para adivinarlo o el ordenador se bloqueara.")

    while intentos > 0:
        try:
        
            numero_usuario = int(input("Introduce tu número: "))
            intentos_usados += 1

            if numero_usuario < 1 or numero_usuario > 20:
                print("Recuerda, ha de ser un número entre 1 y 20.")
                continue

        
            if numero_usuario == numero_secreto:
                print(f"¡Felicidades! Has acertado el número {numero_secreto} en {intentos_usados} intentos.\nEl ordenador se ha desbloqueado y Medusin te lo agradece con un cafe Premium.")
                return
            elif numero_usuario < numero_secreto:
                print(f"El número secreto es mayor que {numero_usuario}.")
            else:
                print(f"El número secreto es menor que {numero_usuario}.")
        except ValueError:
            print("Recuerda, ha de ser un número entre 1 y 20.")
            continue

        intentos -= 1
        print(f"Te quedan {intentos} intento(s).")

    print(f"Lo siento, has perdido. El número secreto era {numero_secreto}. Medusin llora desconsoladamente :( )")


juego_adivinar_numero()
