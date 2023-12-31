import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_valida(palabras):
    #seleccionar una palabra al azar de la lista de palabras validas.
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("="*15)
    print(" "*7,"Bienvenido")
    print("="*15)

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}") 

        # Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        else "-" for letra in palabra]
        #Mostrar estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostrar las letras separadas por un espacio
        print(f"palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                vidas = vidas - 1
                print(f"\n tu letra, {letra_usuario} no está en la palabra")
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra. Por favor escoge una letra nueva. ")
        else: 
            print("\n Esta letra no es válida")
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f" ¡Ahorcado! Perdiste. Lo lamento mucho. la palabra era: {palabra}")
    else: 
        print(f" ¡Excelente! Adivinaste la palabra {palabra}")


ahorcado()
    




