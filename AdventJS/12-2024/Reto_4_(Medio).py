"""
¡Es hora de poner el árbol de Navidad en casa! 🎄 Pero este año queremos que
sea especial. Vamos a crear una función que recibe la altura del árbol (un
entero positivo entre 1 y 100) y un carácter especial para decorarlo.

La función debe devolver un string que represente el árbol de Navidad,
construido de la siguiente manera:

- El árbol está compuesto de triángulos de caracteres especiales.
- Los espacios en blanco a los lados del árbol se representan con guiones
bajos _.
- Todos los árboles tienen un tronco de dos líneas, representado por el
carácter #.
- El árbol siempre debe tener la misma longitud por cada lado.
- Debes asegurarte de que el árbol tenga la forma correcta usando saltos de
línea \n para cada línea.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def create_xmas_tree(height, ornament):
    # Se crea la variable que almacena el arbol
    tree = ''
    # Se calcula el ancho máximo
    max_width = 2*height-1
    # Se itera la cantidad de veces que haya que colocar un ornament
    for i in range(1, height+1):
        # Cantidad de ornamentos a poner
        n_ornament = 2*i-1
        # Cantidad de barra bajas a poner
        n_spaces = int((max_width - n_ornament)/2)
        # Linea del arbol
        tree += '_'*n_spaces + ornament*n_ornament + '_'*n_spaces + '\n'

    # Se añade el tronco
    tree += '_'*int(max_width/2) + chr(35) + '_'*int(max_width/2) + '\n'
    tree += '_'*int(max_width/2) + chr(35) + '_'*int(max_width/2)

    return tree


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    tree = create_xmas_tree(11, '*')
    print(tree)
    pass


if __name__ == "__main__":
    main()
