import random


def jugar():
    print("*"*10)
    print()
    usuario = input("Elige una opción: *pi* para piedra, *pa* para papel y *ti* tijera. \n").lower()
    computadora = random.choice(["pi", "pa", "ti"])

    print()
    print("*"* 10)



    print(f"elegiste {usuario}")


    print(f"computadora elige {computadora}")


    if usuario == computadora:
        return "¡Empate!"

    if gana_jugador(usuario, computadora):
        return "¡Ganaste!" 

    return "¡Perdiste!"


def gana_jugador(jugador, oponente):
    # Retorna True si gana el jugador
    # piedra gana a tijera
    # Tijera gana a papel
    # Pael gana a piedra
    if ((jugador == "pi" and oponente == "ti")
        or (jugador == "ti" and oponente == "pa")
        or (jugador == "pa" and oponente == "pi")):
        return True
    else: 
        return False


print(jugar())