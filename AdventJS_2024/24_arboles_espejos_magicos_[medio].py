"""
En el Polo Norte, los elfos tienen dos árboles binarios mágicos que generan
energía 🌲🌲 para mantener encendida la estrella navideña ⭐️. Sin embargo,
para que funcionen correctamente, los árboles deben estar en perfecta sincronía
como espejos 🪞.

Dos árboles binarios son espejos si:
- Las raíces de ambos árboles tienen el mismo valor.
- Cada nodo del primer árbol debe tener su correspondiente nodo en la posición
opuesta en el segundo árbol.

Y el árbol se representa con tres propiedades "value", "left" y "right".
Dentro de estas dos últimas va mostrando el resto de ramas (si es que tiene):
```python
     tree = {
    "value": '⭐️',
    "left": {
        "value": '🎅'
        # "left": {...}
        # "right": { ... }},
    "right": {
        "value": '🎁'
        # "left": { ... }
        # "right": { ...&nbsp;}}
    }
```

Santa necesita tu ayuda para verificar si los árboles están sincronizados para
que la estrella pueda seguir brillando. Debes devolver un array donde la
primera posición indica si los árboles están sincronizados y la segunda
posición devuelve el valor de la raíz del primer árbol.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def is_trees_synchronized(tree1, tree2):
    # Guarda las variables para los tipos de resultados posibles
    result1, result2 = [], []

    # Se pregunta al inicio si los arboles no tienen el mismo valor
    if tree1['value'] is not tree2['value']:
        return [False, tree1['value']]

    # Se verifica que los arboles sean espejos en todas sus ramas
    if 'left' in tree1 or 'right' in tree2:
        result1 = is_trees_synchronized(tree1['left'], tree2['right'])
    if 'right' in tree1 or 'left' in tree2:
        result2 = is_trees_synchronized(tree1['right'], tree2['left'])

    # Retorna el resultado de la comparación
    if False in result1:
        result1[1] = tree1['value']
        return result1
    elif False in result2:
        result2[1] = tree1['value']
        return result2
    else:
        return [True, tree1['value']]


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    tree1 = {
        "value": '🎄',
        "left": {"value": '⭐'},
        "right": {"value": '🎅'}
    }

    tree2 = {
        "value": '🎄',
        "left": {"value": '🎅'},
        "right": {"value": '⭐'},
    }
    print('+++++++++++++++ TEST 1 +++++++++++++++')
    print(is_trees_synchronized(tree1, tree2))     # [true, '🎄']

    """
       tree1          tree2
        🎄            🎄
        / /           / /
      ⭐   🎅     🎅   ⭐
    """

    tree3 = {
        "value": '🎄',
        "left": {"value": '🎅'},
        "right": {"value": '🎁'}
    }
    print('\n+++++++++++++++ TEST 2 +++++++++++++++')
    print(is_trees_synchronized(tree1, tree3))     # [False, '🎄']

    tree4 = {
       "value": '🎄',
       "left": {"value": '⭐'},
       "right": {"value": '🎅'}
    }

    print('\n+++++++++++++++ TEST 3 +++++++++++++++')
    print(is_trees_synchronized(tree1, tree4))     # [False, '🎄']

    print('\n+++++++++++++++ TEST 4 +++++++++++++++')
    print(is_trees_synchronized(
       {"value": '🎅'},
       {"value": '🧑‍🎄'}))   # [False, '🎅']


if __name__ == "__main__":
    main()
