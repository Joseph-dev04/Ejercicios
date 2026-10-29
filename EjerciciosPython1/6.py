'''ENUNCIADO:
 Escribe una función llamada elemento_mayoritario que reciba una lista de números enteros (numeros) y devuelva el elemento mayoritario de la lista.El elemento mayoritario es aquel número que aparece más de n/2  veces en la lista (donde n es la longitud de la lista). El enunciado te garantiza que el elemento mayoritario siempre existe en la lista de prueba.
 EJEMPLO:
 elemento_mayoritario([3, 2, 3]) -> 3
 elemento_mayoritario([2, 2, 1, 1, 1, 2, 2]) -> 2
 '''

def elemento_mayoritario(numeros: list[int]) -> int:
    if (not isinstance(numeros, list)):
        raise TypeError("No es una lista")
    validador = len(numeros) // 2
    coleccion = {}
    for numero in numeros:
        coleccion[numero] = coleccion.get(numero, 0) + 1
        if (validador < coleccion[numero]):
            return numero

print(elemento_mayoritario([3,2,3]))
print(elemento_mayoritario([2, 2, 1, 1, 1, 2, 2]))