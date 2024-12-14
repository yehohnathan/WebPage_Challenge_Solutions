"""
Ya hemos empaquetado cientos de regalos 🎁… pero a un elfo se le ha olvidado
revisar si el regalo, representado por un asterisco *, está dentro de la caja.

La caja tiene un regalo (*) y cuenta como dentro de la caja si:
- Está rodeada por # en los bordes de la caja.
- El * no está en los bordes de la caja.

Ten en cuenta entonces que el * puede estar dentro, fuera o incluso no estar. Y
debemos devolver true si el * está dentro de la caja y false en caso contrario.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def in_box(box):
    # Se revisa que no haya un regalo entre la primera y ultima linea
    if '*' in list(box[0]) or list(box[-1]):
        return False

    # Ahora se busca que haya un regalo entre las capas
    for line in box:
        line = list(line)
        if '*' in line[1:-1]:
            return True
    return False


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    in_box(["###",
            "#*#",
            "###"])

    in_box(["####",
            "#* #",
            "#  #",
            "####"])

    in_box(["#####",
            "#   #",
            "#  #*",
            "#####"])

    in_box(["#####",
            "#   #",
            "#   #",
            "#   #",
            "#####"])


if __name__ == "__main__":
    main()
