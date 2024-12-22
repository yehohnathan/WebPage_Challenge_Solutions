"""
Santa Claus 🎅 está decorando un árbol de Navidad mágico 🪄, que este año
tiene una estructura especial en forma de árbol binario. Cada nodo del árbol
representa un regalo, y Santa quiere saber la altura del árbol para colocar la
estrella mágica en la punta.

Tu tarea es escribir una función que calcule la altura de un árbol binario. La
altura de un árbol binario se define como el número máximo de niveles desde la
raíz hasta una hoja. Un árbol vacío tiene una altura de 0.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def tree_height(tree: dict):
    # Si el árbol está vacío, se devuelve 0
    if tree is None:
        return 0
    # Se obtiene la altura de cada rama
    left_height = tree_height(tree.get('left'))
    right_height = tree_height(tree.get('right'))
    # Se devuelve la altura máxima entre las ramas
    return 1 + max(left_height, right_height)


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    # Definición del árbol
    tree = {
        'value': '🎁',
        'left': {
            'value': '🎄',
            'left': {
                'value': '⭐',
                'left': None,
                'right': None},
            'right': {
                'value': '🎅',
                'left': None,
                'right': None}},
        'right': {
            'value': '❄️',
            'left': None,
            'right': {
                'value': '🦌',
                'left': None,
                'right': None}}}

    # Representación gráfica del árbol:
    #        🎁
    #       /   \
    #     🎄     ❄️
    #    /  \      \
    #  ⭐   🎅      🦌

    # Llamada a la función
    print(tree_height(tree))
    # Devuelve: 3


if __name__ == "__main__":
    main()
