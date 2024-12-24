"""
Santa Claus 🎅 está revisando una lista de juguetes únicos que podría incluir
en su bolsa mágica de regalos. Quiere explorar todas las combinaciones posibles
de juguetes. Quiere ver todas las combinaciones que realmente contengan al
menos un juguete.

Tu tarea es escribir una función que, dado un array de juguetes, devuelva todas
las combinaciones posibles.

Importante: Debes devolverlo en el orden que aparecen los juguetes y de
combinaciones de 1 a n juguetes.
"""
from itertools import combinations


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def generate_gift_sets_library(gifts):
    all_combinations = []
    for i in range(1, len(gifts) + 1):
        print(all_combinations)
        all_combinations.extend(
            [list(combo) for combo in combinations(gifts, i)])
    return all_combinations


def generate_gift_sets(gifts):
    ans = []

    def backtracking(idx: int = 0, curr: list[str] = []):
        if len(curr) > 0:
            ans.append(curr[:])

        for i in range(idx, len(gifts)):
            curr.append(gifts[i])
            backtracking(i + 1, curr)
            curr.pop()

    backtracking()
    ans.sort(key=len)
    return ans


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print(generate_gift_sets(['car', 'doll', 'puzzle']))
    # [
    #   ['car'],
    #   ['car', 'doll'],
    #   ['car', 'doll', 'puzzle'],
    #   ['car', 'puzzle'],
    #   ['doll'],
    #   ['doll', 'puzzle'],
    #   ['puzzle']
    # ]

    print(generate_gift_sets(['ball']))
    # [
    #   ['ball']
    # ]

    print(generate_gift_sets(['game', 'pc']))
    # [
    #   ['game'],
    #   ['game', 'pc'],
    #   ['pc']
    # ]


if __name__ == "__main__":
    main()
