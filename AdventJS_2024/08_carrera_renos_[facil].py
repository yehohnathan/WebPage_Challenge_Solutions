"""
¡Es hora de seleccionar a los renos más rápidos para los viajes de Santa! 🦌🎄
Santa Claus ha organizado unas emocionantes carreras de renos para decidir
cuáles están en mejor forma.

Tu tarea es mostrar el progreso de cada reno en una pista de nieve en formato
isométrico.

La información que recibes:
- indices: Un array de enteros que representan el progreso de cada reno en la
pista:
    - 0: El carril está vacío.
    - Número positivo: La posición actual del reno desde el inicio de la pista.
    - Número negativo: La posición actual del reno desde el final de la pista.
- length: La longitud de cada carril.

Devuelve un string que represente la pista de la carrera:
- Cada carril tiene exactamente length posiciones llenas de nieve (~).
- Cada reno se representa con la letra r.
- Los carriles están numerados al final con /1, /2, etc.
- La vista es isométrica, por lo que los carriles inferiores están desplazados
hacia la derecha.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
# Solución utilizando arrays
def draw_race_array(indices, length):
    # Variable que guarde el contenido de carrera
    carrera = []
    # Cantidad de participantes
    n_renos = len(indices)
    # Carril original
    carril = ['~'] * length
    # Se repite el ciclo según la cantidad de renos
    for i in range(n_renos):
        reno = indices[i]           # Posición del reno
        posicion = carril[:]        # Se restaura la carretera
        if reno > 0:
            posicion[reno] = 'r'    # Se remplaza la posición del reno
        elif reno < 0:
            posicion[length+reno] = 'r'
        linea = ' '*(n_renos - i - 1) + ''.join(posicion) + f' /{i+1}'
        carrera.append(linea)

    return '\n'.join(carrera)


# Solución 2 utilizando arrays -> Más eficiente
def draw_race(indices, length):
    # Variable que guarde el contenido de carrera
    carrera = []
    # Cantidad de participantes
    n_renos = len(indices)
    # Se repite el ciclo según la cantidad de renos
    for i in range(n_renos):
        reno = indices[i]           # Posición del reno
        if reno == 0:
            linea = "~" * length
        if reno != 0:
            abs_renos = reno if reno > 0 else length + reno
            linea = "~" * abs_renos + "r" + "~" * (length - abs_renos - 1)
        linea = f'{' '*(n_renos - i - 1)}{linea} /{i + 1}'
        carrera.append(linea)

    return '\n'.join(carrera)


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print(draw_race([0, 5, -3], 10))

    print(draw_race([2, -1, 0, 5], 8))

    print(draw_race([3, 7, -2], 12))


if __name__ == "__main__":
    main()
