""" ENUNCIADO:
Crea una clase llamada Solucion con un metodo estatico llamado fizz_buzz. Este metodo debe recibir un numero entero (n) y devolver una cadena de 
texto (String) segun las siguientes reglas:

Si el numero es divisible por 3, debe devolver "Fizz".
Si el numero es divisible por 5, debe devolver "Buzz".
Si es divisible por ambos (3 y 5), debe devolver "FizzBuzz".
Si no es divisible por ninguno de ellos, debe devolver el numero convertido en texto (por ejemplo, si entra 7, devuelve "7").

Ejemplos de entrada y salida:
fizz_buzz(3) deberia devolver "Fizz"
fizz_buzz(5) deberia devolver "Buzz"
fizz_buzz(15) deberia devolver "FizzBuzz"
fizz_buzz(7) deberia devolver "7"
"""

class Solution:

    @staticmethod
    def fizz_buzz(n : int) -> str:
        if (n % 5 == 0 and n % 3 == 0):
            return "FizzBuzz"
        if (n % 5 == 0):
            return "Buzz"
        if (n % 3 == 0):
            return "Fizz"
        else:
            return str(n)

if __name__ == "__main__":
    print(Solution.fizz_buzz(3))
    print(Solution.fizz_buzz(5))
    print(Solution.fizz_buzz(15))
    print(Solution.fizz_buzz(7))