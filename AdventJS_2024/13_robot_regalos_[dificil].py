"""
Los elfos del Polo Norte han creado un robot 🤖 especial que ayuda a Papá Noel
a distribuir regalos dentro de un gran almacén. El robot se mueve en un plano
2D y partimos desde el origen (0, 0).

Queremos saber si, tras ejecutar una serie de movimientos, el robot vuelve a
estar justo donde empezó.

Las órdenes básicas del robot son:
- L: Mover hacia la izquierda
- R: Mover hacia la derecha
- U: Mover hacia arriba
- D: Mover hacia abajo

Pero también tiene ciertos modificadores para los movimientos:
- *: El movimiento se realiza con el doble de intensidad (ej: *R significa RR)
- !: El siguiente movimiento se invierte (ej: R!L se considera como RR)
- ?: El siguiente movimiento se hace sólo si no se ha hecho antes (ej: R?R
significa R)

Nota: Cuando el movimiento se invierte con ! se contabiliza el movimiento
invertido y no el original. Por ejemplo, !U?U invierte el movimiento de U, por
lo que contabiliza que se hizo el movimiento D pero no el U. Así !U?U se
traduce como D?U y, por lo tanto, se haría el movimiento U final.

Debes devolver:

- true: si el robot vuelve a estar justo donde empezó
- [x, y]: si el robot no vuelve a estar justo donde empezó, devolver la
posición donde se detuvo
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def is_robot_back(moves: list[str]) -> bool | list[int]:
    # Convierte move en una lista para su facil manipulación (reemplazar)
    moves = list(moves)
    # Variable que contiene la posición del rebot
    posicion = [0, 0]
    # Diccionario para contar los movimientos
    contador_moves = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
    # Diccionario movimientos opuestos
    opuesto_moves = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
    # Ciclo para los movimientos del robot
    mod = 1    # Modificador del movimiento
    for i, char in enumerate(moves):
        if char == '*':
            mod = 2
        elif char == '?':
            if contador_moves[moves[i + 1]] != 0:
                mod = 0
        elif char == '!':
            moves[i + 1] = opuesto_moves[moves[i + 1]]
        else:
            contador_moves[char] += 1 * mod
            mod = 1

    # Se suma los movimientos
    posicion[0] = contador_moves['R'] - contador_moves['L']
    posicion[1] = contador_moves['U'] - contador_moves['D']

    return True if posicion == [0, 0] else posicion


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    is_robot_back('R')        # [1, 0]
    is_robot_back('RL')       # true
    is_robot_back('RLUD')     # true
    is_robot_back('*RU')      # [2, 1]
    is_robot_back('R*U')      # [1, 2]
    is_robot_back('LLL!R')    # [-4, 0]
    is_robot_back('R?R')      # [1, 0]
    is_robot_back('U?D')      # true
    is_robot_back('R!L')      # [2,0]
    is_robot_back('U!D')      # [0,2]
    is_robot_back('R?L')      # true
    is_robot_back('U?U')      # [0,1]
    is_robot_back('*U?U')     # [0,2]
    is_robot_back('U?D?U')    # true

    # Ejemplos paso a paso:
    is_robot_back('R!U?U')      # [1,0]
    # 'R'  -> se mueve a la derecha
    # '!U' -> se invierte y se convierte en 'D'
    # '?U' -> se mueve arriba, porque no se ha hecho el movimiento 'U'

    is_robot_back('UU!U?D')     # [0,1]
    # 'U'  -> se mueve arriba
    # 'U'  -> se mueve arriba
    # '!U' -> se invierte y se convierte en 'D'
    # '?D' -> no se mueve, ya que ya se hizo el movimiento 'D'


if __name__ == "__main__":
    main()
