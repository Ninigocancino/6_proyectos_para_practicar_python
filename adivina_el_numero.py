import random


def adivina_el_numero(x):
    print("**" * 6)
    print("    ¡Bienvenido(a) al juego!")
    print("**" * 6)
    print("Tu meta es adivinar el número que la computadora ha elegido")

    numero_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y "x".

    jugador = 0

    while jugador != numero_aleatorio:
        # El usuario ingresa un numero
        jugador = int(input(f"Adivina un número entre 1 y {x}: "))

        if jugador < numero_aleatorio:
            print("Intenta otra vez. este numero es muy pequeño")
        elif jugador > numero_aleatorio:
            print("Intenta de nuevo. Este numewro es muy grande.")

    print(f"¡Felicitaciones! Adivinaste, el numero es {numero_aleatorio} correctamente")


adivina_el_numero(10)