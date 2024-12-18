"""
El Grinch ha estado haciendo de las suyas en el Polo Norte y ha sembrado bombas
de carbón explosivo 💣 en la fábrica de juguetes de los duendes. Quiere que
todos los juguetes queden inutilizados y por eso ha dejado una cuadrícula donde
algunas celdas tienen carbón explosivo (True) y otras están vacías (False).

Los duendes necesitan tu ayuda para mapear las zonas peligrosas. Cada celda
vacía debe mostrar un número que indique cuántas bombas de carbón explosivo hay
en las posiciones adyacentes, incluidas las diagonales.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    # Tamaño de columnas y filas
    s_row, s_columns = len(grid), len(grid[0])
    # Se crea una lista de listas para los resultados
    resultado = [[0 for i in range(s_row)] for j in range(s_columns)]
    # Coordenadas para buscar en casillas adyacentes
    coordenadas = [[-1, -1], [-1, 0], [-1, 1],
                   [0, -1],           [0, 1],
                   [1, -1],  [1, 0],  [1, 1]]

    # Ciclo para ir sumando las detecciones de carbón explosivo
    for i in range(s_row):
        for j in range(s_columns):
            # Si se detectó un True, se suma las casillas adyacentes
            if grid[i][j]:
                for coor in coordenadas:
                    xi, xj = i + coor[0], j + coor[1]
                    if (0 <= xi < s_row) and (0 <= xj < s_columns):
                        resultado[xi][xj] += 1
    return resultado


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    detect_bombs([
        [True, False, False],
        [False, True, False],
        [False, False, False]])
    # [
    #   [1, 2, 1],
    #   [2, 1, 1],
    #   [1, 1, 1]
    # ]

    detect_bombs([
        [True, False],
        [False, False]])
    # [
    #   [0, 1],
    #   [1, 1]
    # ]


if __name__ == "__main__":
    main()
