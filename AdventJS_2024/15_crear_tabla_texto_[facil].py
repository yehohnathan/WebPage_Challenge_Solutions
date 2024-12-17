"""
Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una
aplicación de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un
array de objetos y lo convierta en una tabla de texto.

La tabla dibujada debe representar los datos del objeto de la siguiente manera:
- Tiene una cabecera con el nombre de la columna.
- El nombre de la columna pone la primera letra en mayúscula.
- Cada fila debe contener los valores de los objetos en el orden
correspondiente.
- Cada valor debe estar alineado a la izquierda.
- Los campos dejan siempre un espacio a la izquierda.
- Los campos dejan a la derecha el espacio necesario para alinear la caja.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def draw_table(data: list[dict[str, str | int]]) -> str:
    # Obtener los nombres de las columnas
    columns = [col.capitalize() for col in data[0].keys()]

    # Encuentra el tamaño máximo de ancho por columna según las filas
    col_widths = [max(len(str(row[col])) for row in data
                      ) for col in data[0].keys()]

    # Discrimida el ancho máximo de la fila encontrado por el ancho del titulo
    col_widths = [max(len(col), width) for col, width in zip(columns,
                                                             col_widths)]

    # Crear la cabecera de la tabla
    header = ' | '.join(col.ljust(width) for col, width in zip(
        columns, col_widths))
    separator = '+-' + '-+-'.join('-' * width for width in col_widths) + '-+'

    # Crear las filas de la tabla
    rows = []       # Guarda las filas
    for row in data:
        rows.append(
            ' | '.join(str(row[col]).ljust(width) for col, width in zip(
                data[0].keys(), col_widths)))

    # Unir todas las partes de la tabla
    table = [separator, f'| {header} |', separator] + [
        f'| {row} |' for row in rows] + [separator]

    return '\n'.join(table)


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    # Ejemplo de uso:
    data1 = [
        {"name": "Alice", "city": "London"},
        {"name": "Bob", "city": "Paris"},
        {"name": "Charlie", "city": "New York"}
    ]

    data2 = [
        {"game": "indiajones", "subtitle": 'the game'},
        {"game": "pokemosblue", "subtitle": ''},
    ]

    print(draw_table(data1))
    print(draw_table(data2))


if __name__ == "__main__":
    main()
