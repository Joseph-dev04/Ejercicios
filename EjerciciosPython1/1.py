""" ENUNCIADO:
Tu tarea es escribir una funcion llamada celsius_a_fahrenheit que reciba como parametro una temperatura en grados Celsius (puede ser un numero 
entero o decimal) y devuelva su equivalente en grados Fahrenheit.
La formula de conversion es: f = c * 9/5 + 32

Ejemplos de entrada y salida:
celsius_a_fahrenheit(0) deberia devolver 32.0
celsius_a_fahrenheit(20) deberia devolver 68.0
celsius_a_fahrenheit(-10) deberia devolver 14.0
"""

def celsius_a_fahrenheit(celsius: float) -> float:
    return celsius * 9/5 + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit(0))
    print(celsius_a_fahrenheit(20))
    print(celsius_a_fahrenheit(-10))
    