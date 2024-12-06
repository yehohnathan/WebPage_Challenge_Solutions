"""
Santa Claus 🎅 quiere enmarcar los nombres de los niños buenos para decorar su
taller 🖼️, pero el marco debe cumplir unas reglas específicas. Tu tarea es
ayudar a los elfos a generar este marco mágico.

Reglas:
- Dado un array de nombres, debes crear un marco rectangular que los contenga a
todos.
- Cada nombre debe estar en una línea, alineado a la izquierda.
- El marco está construido con * y tiene un borde de una línea de ancho.
- La anchura del marco se adapta automáticamente al nombre más largo más un
margen de 1 espacio a cada lado.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def createFrame(names):
    max_size = len(max(names, key=len)) + 4
    start_end_frame = '*'*(max_size)
    frame = start_end_frame
    for name in names:
        temp = f'* {name}'
        temp = temp + ' '*(max_size - len(temp) - 1) + '*'
        frame += f'\n{temp}'
    frame += f'\n{start_end_frame}'
    print(frame)
    return frame


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    createFrame(['midu', 'madeval', 'educalvolpz'])
    createFrame(['midu'])
    createFrame(['a', 'bb', 'ccc'])
    createFrame(['a', 'bb', 'ccc', 'dddd'])


if __name__ == "__main__":
    main()
