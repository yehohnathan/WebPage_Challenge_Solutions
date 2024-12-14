"""
Los elfos 🧝🧝‍♂️ de Santa Claus han encontrado un montón de botas mágicas
desordenadas en el taller. Cada bota se describe por dos valores:
- type indica si es una bota izquierda (I) o derecha (R).
- size indica el tamaño de la bota.
Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño que
tengan izquierda y derecha. Para ello, debes devolver una lista con los pares
disponibles después de emparejar las botas.

¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo
tamaño!
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def organizeShoes(shoes):
    # Diccionario para contar tipos por tamaño
    shoe_counts = {}

    # Contar botas izquierda (I) y derecha (R) por tamaño
    for shoe in shoes:
        if shoe['size'] not in shoe_counts:
            shoe_counts[shoe['size']] = {'I': 0, 'R': 0}
        shoe_counts[shoe['size']][shoe['type']] += 1

    # Calcular pares disponibles
    available_pairs = []
    for size, counts in shoe_counts.items():
        pairs = min(counts['I'], counts['R'])  # Emparejar por el menor conteo
        available_pairs.extend([size] * pairs)

    return available_pairs


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    shoes = [
        {'type': 'I', 'size': 38},
        {'type': 'R', 'size': 38},
        {'type': 'R', 'size': 42},
        {'type': 'I', 'size': 41},
        {'type': 'I', 'size': 42}]
    print(organizeShoes(shoes))

    shoes2 = [
        {'type': 'I', 'size': 38},
        {'type': 'R', 'size': 38},
        {'type': 'I', 'size': 38},
        {'type': 'I', 'size': 38},
        {'type': 'R', 'size': 38}]
    organizeShoes(shoes2)

    shoes3 = [
        {'type': 'I', 'size': 38},
        {'type': 'R', 'size': 36},
        {'type': 'R', 'size': 42},
        {'type': 'I', 'size': 41},
        {'type': 'I', 'size': 43}]
    organizeShoes(shoes3)


if __name__ == "__main__":
    main()
