"""
Santa Claus 🎅 está revisando la lista de regalos que debe entregar esta
Navidad. Sin embargo, algunos regalos faltan, otros están duplicados, y algunos
tienen cantidades incorrectas. Necesita tu ayuda para resolver el problema.

Recibirás dos arrays:
- received: Lista con los regalos que Santa tiene actualmente.
- expected: Lista con los regalos que Santa debería tener.

Tu tarea es escribir una función que, dado received y expected, devuelva un
objeto con dos propiedades:
- missing: Un objeto donde las claves son los nombres de los regalos faltantes
y los valores son las cantidades que faltan.
- extra: Un objeto donde las claves son los nombres de los regalos extra o
duplicados y los valores son las cantidades que sobran.

Ten en cuenta que:
- Los regalos pueden repetirse en ambas listas.
- Las listas de regalos están desordenadas.
- Si no hay regalos que falten o sobren, las propiedades correspondientes
(missing o extra) deben ser objetos vacíos.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def fix_gift_list(received: list[str], expected: list[str]) -> dict[str, int]:
    # Lista de regalos faltantes y sobrantes
    gift_list = {"missing": {}, "extra": {}}

    # Se recorren todos los regalos registrdos
    for toy in set(received + expected):
        if toy not in received:
            gift_list.setdefault("missing", {})[toy] = expected.count(toy)
        elif received.count(toy) < expected.count(toy):
            gift_list.setdefault(
                "missing", {})[toy] = expected.count(toy) - received.count(toy)
        elif received.count(toy) > expected.count(toy):
            gift_list.setdefault(
                "extra", {})[toy] = received.count(toy) - expected.count(toy)

    return gift_list


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    fix_gift_list(
        ['puzzle', 'car', 'doll', 'car'],
        ['car', 'puzzle', 'doll', 'ball'])
    # Devuelve:
    # {
    #   missing: { ball: 1 },
    #   extra: { car: 1 }
    # }

    fix_gift_list(
        ['book', 'train', 'kite', 'train'],
        ['train', 'book', 'kite', 'ball', 'kite'])
    # Devuelve:
    # {
    #   missing: { ball: 1, kite: 1 },
    #   extra: { train: 1 }
    # }

    fix_gift_list(
        ['bear', 'bear', 'car'],
        ['bear', 'car', 'puzzle', 'bear', 'car', 'car'])
    # Devuelve:
    # {
    #   missing: { puzzle: 1, car: 2 },
    #   extra: {}
    # }

    fix_gift_list(
        ['bear', 'bear', 'car'],
        ['car', 'bear', 'bear'])
    # Devuelve:
    # {
    #   missing: {},
    #   extra: {}
    # }


if __name__ == "__main__":
    main()
