""" ENUNCIADO:
Tu tarea es escribir una funcion llamada contar_vocales que reciba una cadena de texto (string) y devuelva un numero entero que represente 
la cantidad total de vocales que contiene esa cadena.

Reglas:
Las vocales son: a, e, i, o, u.
Tu funcion debe ser capaz de contar tanto las vocales minusculas como las mayusculas (A, E, I, O, U).
Los espacios, numeros o signos de puntuacion no deben contarse.

Ejemplos de entrada y salida:
contar_vocales("Python") deberia devolver 1 (la 'o').
contar_vocales("LeetCode") deberia devolver 4 (e, e, o, e).
contar_vocales("Prueba de TEXTO") deberia devolver 6 (u, e, a, e, e, o).
"""

def contar_vocales(palabra: str) -> int:
    return sum(1 for letra in palabra.lower() if letra in "aeiou")

if __name__ == "__main__":
    print(contar_vocales("Python"))
    print(contar_vocales("LeetCode"))
    print(contar_vocales("Prueba de TEXTO"))