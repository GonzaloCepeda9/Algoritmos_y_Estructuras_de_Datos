"""
22. El problema de la mochila Jedi.
Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos objetos.
Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila.

◘ Algoritmo para resolver el problema:
  Crear un contador para saber cuántos elementos fue necesario sacar hasta encontrar el sable de luz.
  Siendo la mochila una lista, comparar:
    Si la mochila está vacía, devolver mensaje.
      - Devolver mensaje "La mochila está vacía. No se encontró el sable de luz".
    
    Si el elemento sacado es "sable de luz":
      - Devolver el mensaje "Jedi encontró su sable de luz".
      - Devolver el contador de objetos sacados + 1.
    
    Si no es "sable de luz":
      - Eliminar el último elemento de la lista y llamar a la función nuevamente.
      - Sumar uno a al contador de objetos sacados.
"""

mochila_Jedi = [
  "sable de luz",
  "comunicador",
  "capa",
  "mapa",
  "linterna",
  "cuerda",
  "piedra",
  "par de guantes",
  "botiquín"
]

def usar_la_fuerza(mochila: list, sacados: int = 0):
  if len(mochila) == 0:
    return "\nLa mochila está vacía. No se encontró el sable de luz."
  elif mochila[-1] == "sable de luz":
    return f"\nJedi encontró su sable de luz. Fue necesario sacar {sacados + 1} elemento/s hasta encontrarlo."
  else:
    print(mochila)
    return f"\nJedi sacó su {mochila[-1]}." + usar_la_fuerza((mochila[:-1]), (sacados + 1))


print("\n--------------------------------------------- Función: Encontrar sable de luz ---------------------------------------------")
busqueda = usar_la_fuerza(mochila_Jedi)
print(busqueda)