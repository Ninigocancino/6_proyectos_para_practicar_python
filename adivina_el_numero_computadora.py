import random


def adivina_el_numero_computadora(x):

    print("============================")
    print("  Bienvenido(a) al jauego!")
    print("============================")
    print(f"Selecciona un numero entre 1 y el valor de {x} para que la computadora intente adivinarlo")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else: 
            prediccion = limite_inferior #aunque tambien podría ser el limite superior porque ambos son iguales

        # Obtener una respuesta del usuario
        respuesta = input(f"Mi predicción es {prediccion}. si es muy alta, ingres (A), si es muy baja, ingresa (B). si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"¡Siiiii!, la computadora adivinó tu numero correctamente: {prediccion}") 


adivina_el_numero_computadora(10)       
        