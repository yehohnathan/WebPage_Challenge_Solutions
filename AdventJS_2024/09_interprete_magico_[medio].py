"""
Los elfos están jugando con un tren 🚂 mágico que transporta regalos. Este
tren se mueve en un tablero representado por un array de strings.

El tren está compuesto por una locomotora (@), seguida de sus vagones (o), y
debe recoger frutas mágicas (*) que le sirve de combustible. El movimiento del
tren sigue las siguientes reglas:

Recibirás dos parámetros board y mov.

board es un array de strings que representa el tablero:
- @ es la locomotora del tren.
- o son los vagones del tren.
- * es una fruta mágica.
- · son espacios vacíos.

mov es un string que indica el próximo movimiento del tren desde la cabeza del
tren @:

- 'L': izquierda
- 'R': derecha
- 'U': arriba
- 'D': abajo.

Con esta información, debes devolver una cadena de texto:
- 'crash': Si el tren choca contra los bordes del tablero o contra sí mismo.
- 'eat': Si el tren recoge una fruta mágica (*).
- 'none': Si avanza sin chocar ni recoger ninguna fruta mágica.
"""
# ++++++++++++++++++++++++++++++ # LIBRERÍAS # ++++++++++++++++++++++++++++++ #
from typing import List, Literal    # Unicamente para reestringir los pámetros


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
# Solución 1:
def move_train_1(board: List[str], mov: Literal['U', 'D', 'R', 'L']
                 ) -> Literal['none', 'crash', 'eat']:
    # Diccionario con las posibles opciones
    opciones = {'*': 'eat', '·': 'none', 'o': 'crash'}
    # Hago un ciclo flor, necesito encontrar donde esta la locomotora
    for i, piece in enumerate(board):
        # Encuentro la cabeza
        if '@' in piece:
            i_locomotora = piece.find('@')
            if mov == 'U':
                i -= 1
            elif mov == 'D':
                i += 1
            elif mov == 'R':
                i_locomotora += 1
            elif mov == 'L':
                i_locomotora -= 1

            # Verificar si 'i' está fuera de los límites del tablero
            if i < 0 or (i + 1) > len(board):
                return 'crash'

            # Verificar si 'i_locomotora' está fuera de los límites de las
            # piezas
            if i_locomotora < 0 or (i_locomotora + 1) > len(piece):
                return 'crash'

            return opciones[board[i][i_locomotora]]

    return 'none'


# Solución 2:
def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']
               ) -> Literal['none', 'crash', 'eat']:
    # Se puede observar en la Solución 1 que los if con 'mov', que cada letra
    # tiene de operación. Eso puede ser otro diccionario.
    movimiento = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    # Se extrae el tipo de 'movimiento' de movimiento
    i_mov, i_loco_mov = movimiento[mov]
    # Hago un ciclo flor, necesito encontrar donde esta la locomotora
    for i, piece in enumerate(board):
        # Encuentro la cabeza
        if '@' in piece:
            i_loco = piece.find('@')
            break

    # Guardo el valor de los indices
    new_i_mov, new_i_loco_mov = i + i_mov, i_loco + i_loco_mov

    # Verificar límites
    if not (0 <= new_i_mov < len(board)) or not (
            0 <= new_i_loco_mov < len(board[0])):
        return 'crash'

    # Esto es más rápido que usar el diccionario 'opciones'
    result = board[new_i_mov][new_i_loco_mov]
    return {'*': 'eat', '·': 'none', 'o': 'crash'}.get(result, 'crash')


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    board = ['·····', '*····', '@····', 'o····', 'o····']

    print(move_train(board, 'U'))
    # ➞ 'eat'
    # Porque el tren se mueve hacia arriba y encuentra una fruta mágica

    print(move_train(board, 'D'))
    # ➞ 'crash'
    # El tren se mueve hacia abajo y la cabeza se choca consigo mismo

    print(move_train(board, 'L'))
    # ➞ 'crash'
    # El tren se mueve a la izquierda y se choca contra la pared

    print(move_train(board, 'R'))
    # ➞ 'none'
    # El tren se mueve hacia derecha y hay un espacio vacío en la derecha


if __name__ == "__main__":
    main()
