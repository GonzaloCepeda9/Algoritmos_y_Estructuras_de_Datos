"""
20. Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son cantidad de pasos y dirección (suponga que el robot solo puede moverse en ocho direcciones: norte, sur, este, oeste, noreste, noroeste, sureste y suroeste).
Luego desarrolle otro algoritmo que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida, retornando por el mismo camino que fue.
"""

from stack import Stack

movimientos = Stack()

movimiento_contrario = {
    'norte': 'sur',
    'sur': 'norte',
    'este': 'oeste',
    'oeste': 'este',
    'noreste': 'suroeste',
    'suroeste': 'noreste',
    'noroeste': 'sureste',
    'sureste': 'noroeste',
}

print('\n--------------------------------------------- Registro de movimientos del robot: ---------------------------------------------')
movimiento_ingresado = input('Ingrese los pasos y dirección del movimiento separados por un espacio (ejemplo: 9 sur ): ')

# Registrar movimientos de un robot (paso y dirección):
while movimiento_ingresado != 'fin':

    datos = movimiento_ingresado.split() # Divide la cadena ingresada por espacios, y devuelve una lista con los elementos.

    if len(datos) > 1:
        pasos = int(datos[0]) # Si no ingresa un número, el programa lanza error. Esto no se puede corregir sin try-except, todavía no lo hemos dado.
        direccion = datos[1]
        print(f'El robot se movió {pasos} paso/s hacia el {direccion}.')

        movimiento = pasos, direccion
        movimientos.push(movimiento)

    movimiento_ingresado = input('Ingrese los pasos y dirección del movimiento separados por un espacio (ejemplo: 9 sur ): ')

print('Secuencia de movimientos finalizada.')

# Generar la secuencia de movimientos necesarios para hacer volver al robot a su lugar de partida:
print('\n-------------------- Secuencia de movimientos necesaria para hacer volver al robot a su punto de partida: --------------------')
while movimientos.size() > 0:
    pasos, direccion = movimientos.pop()
    direccion_contraria = movimiento_contrario[direccion]

    print(f'El robot debe moverse {pasos} paso/s hacia el {direccion_contraria}.')