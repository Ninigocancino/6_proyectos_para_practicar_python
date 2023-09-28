# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# Aprender a programar con _____________.

"""
organizacion = "freeCodeCamp"

print("Aprende a programar con " + organizacion)
print("Aprende a programar con {}".format(organizacion))
print(f"Aprende a programar con {organizacion}")

"""

# Mad Libs (Historias Locas)

print("__" * 15)
adj_1 = input("Ingresa un adjetivo: ")
verbo_1 = input("Ingresa un verbo: ")
organizacion = input("ingresa una organización: ")
verbo_2 = input("Ingresa otro verbo: ")
sustantivo_plural = input("Agrega un sustantivo en plural: ")

print(" ")

madlib = f"¡Programar es tan adj {adj_1}!siempre me emociona porque me encanta {verbo_1} problemas. ¡Aprende a {verbo_2} con {organizacion} y alcanza tus {sustantivo_plural}!"

print(" ")
print(madlib)