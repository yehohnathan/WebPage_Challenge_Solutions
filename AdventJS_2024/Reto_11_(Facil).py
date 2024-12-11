"""
El Grinch ha hackeado 🏴‍☠️ los sistemas del taller de Santa Claus y ha
codificado los nombres de todos los archivos importantes. Ahora los elfos no
pueden encontrar los archivos originales y necesitan tu ayuda para descifrar
los nombres.

Cada archivo sigue este formato:
- Comienza con un número (puede contener cualquier cantidad de dígitos).
- Luego tiene un guion bajo _.
- Continúa con un nombre de archivo y su extensión.
- Finaliza con una extensión extra al final (que no necesitamos).

Ten en cuenta que el nombre de los archivos pueden contener letras (a-z, A-Z),
números (0-9), otros guiones bajos (_) y guiones (-).

Tu tarea es implementar una función que reciba un string con el nombre de un
archivo codificado y devuelva solo la parte importante: el nombre del archivo y
su extensión.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def decode_filename(filename: str) -> str:
    # Se encuentra el indice donde empieza el nombre del archivo
    index_name = filename.find('_') + 1
    # Se encuentra el indice donde empieza el .extensión
    true_extension = filename.find('.')
    # Se encuentra el indice donde empieza el .extensión falso
    false_extension = filename[true_extension+1:].find('.') + 1
    # Se retorna el string filtrado
    return filename[index_name:true_extension+false_extension]


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    decode_filename('2023122512345678_sleighDesign.png.grinchwa')
    # ➞ "sleighDesign.png"

    decode_filename('42_chimney_dimensions.pdf.hack2023')
    # ➞ "chimney_dimensions.pdf"

    decode_filename('987654321_elf-roster.csv.tempfile')
    # ➞ "elf-roster.csv"


if __name__ == "__main__":
    main()
