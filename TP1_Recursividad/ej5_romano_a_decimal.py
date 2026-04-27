"""
5. Desarrollar una función que permita convertir un número romano en un número decimal.

◘ Algoritmo para resolver el problema:
    CASO IDEAL (números válidos):
    - Si el caracter en posición 0 es menor que el caracter en posición 1, restar caracter 0 a caracter 1. Devolver cadena sin ambos valores (desde posición 2 hasta el final).
    - Si no, sumar caracter 0; y devolver cadena sin el primero (desde posición 1 hasta el final).
    CASO PARTICULAR (excepción):
    - Si el número ingresado tiene sólo 1 caracter, y es válido, devolver directamente la equivalencia del número.
"""

print("\n---------------------------------------- Función: Convertir número romano a decimal ---------------------------------------")

equivalencias = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def conversion(romano):
    if len(romano) == 0:
        return 0
    elif len(romano) == 1:
        return equivalencias[romano[0]]
    elif len(romano) > 1:
        if (equivalencias[romano[0]] < equivalencias[romano[1]]):
            return equivalencias[romano[1]] - equivalencias[romano[0]] + conversion(romano[2:])
        else:
            return equivalencias[romano[0]] + conversion(romano[1:])
    
resultado1 = conversion("IX")
resultado2 = conversion("XVIII")
resultado3 = conversion("XXVII")
resultado4 = conversion("XCIX")
resultado5 = conversion("CXLV")
resultado6 = conversion("DCLIV")
resultado7 = conversion("MCMXCIV")

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)