"""
Santa Claus 🎅 ha recibido una lista de números mágicos que representan
regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para
evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente
antes de entregárselos a los elfos.

Tu tarea es escribir una función que reciba una lista de números enteros (que
pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada
en orden ascendente.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def prepare_gifts(gifts):
    return list(set(gifts))


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    gifts1 = [3, 1, 2, 3, 4, 2, 5]
    print(prepare_gifts(gifts1))

    gifts2 = [6, 5, 5, 5, 5]
    print(prepare_gifts(gifts2))

    gifts3 = []
    print(prepare_gifts(gifts3))


if __name__ == "__main__":
    main()
