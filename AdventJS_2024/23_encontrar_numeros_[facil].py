"""
Los elfos están trabajando en un sistema para verificar las listas de regalos
de los niños 👧👦. Sin embargo, ¡algunas listas están incompletas y faltan
números!

Tu tarea es escribir una función que, dado un array de números, encuentre todos
los números que faltan entre 1 y n (donde n es el tamaño del array o el número
más alto del array).

Eso sí, ten en cuenta que:
- Los números pueden aparecer más de una vez y otros pueden faltar
- El array siempre contiene números enteros positivos
- Siempre se empieza a contar desde el 1
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def find_missing_numbers(nums):
    # Guarda los números faltantes
    missing = list(range(1, max(nums)+1))
    # Ciclo del tamaño del número máximo de nums
    for i in set(nums):
        missing.remove(i)
    return missing


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print(find_missing_numbers([1, 2, 4, 6]))
    # [3, 5]

    print(find_missing_numbers([4, 8, 7, 2]))
    # [1, 3, 5, 6]

    print(find_missing_numbers([3, 2, 1, 1]))
    # []

    print(find_missing_numbers([5, 5, 5, 3, 3, 2, 1]))
    # [4]


if __name__ == "__main__":
    main()
