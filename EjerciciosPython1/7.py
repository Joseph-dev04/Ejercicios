'''ENUNCIADO:
Escribe una función llamada es_valido que reciba una cadena de texto (cadena) que contiene únicamente los caracteres (, ), {, }, [ y ]. La función debe determinar si la cadena de entrada es válida.

Una cadena es válida si:
Los paréntesis de apertura deben cerrarse con el mismo tipo de paréntesis.
Los paréntesis de apertura deben cerrarse en el orden correcto.
Todo paréntesis de cierre tiene un paréntesis de apertura correspondiente del mismo tipo.
PRUEBAS:
es_valido("()") -> True
es_valido("()[]{}") -> True
es_valido("(]") -> False
es_valido("([)]") -> False (Se cruzan de forma incorrecta).
es_valido("{[]}") -> True (Anidados correctamente).
'''

def es_valido(cadena: str) -> bool:
    if not isinstance(cadena, str):
        raise TypeError("No es una cadena de texto")
    pila = []
    llaves = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }
    for simbolo in cadena:
        if simbolo in llaves:
            if pila and pila[-1] == llaves[simbolo]:
                pila.pop()
            else:
                return False
        else:
            pila.append(simbolo)
    return len(pila) == 0

print(es_valido("()"))
print(es_valido("()[]{}"))
print(es_valido("(]"))
print(es_valido("([)]"))
print(es_valido("{[]}"))