"""
Los elfos están trabajando arduamente para limpiar los caminos llenos de nieve
mágica ❄️. Esta nieve tiene una propiedad especial: si dos montículos de nieve
idénticos y adyacentes se encuentran, desaparecen automáticamente.

Tu tarea es escribir una función que ayude a los elfos a simular este proceso.
El camino se representa por una cadena de texto y cada montículo de nieve un
carácter.

Tienes que eliminar todos los montículos de nieve adyacentes que sean iguales
hasta que no queden más movimientos posibles.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def remove_snow(s: str) -> str:
    # Ciclo que se termina hasta que i sea de tamaño del string
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s.replace(s[i:i+2], '')
            i = 0
        else:
            i += 1
    print(s)
    return s


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():

    remove_snow('zxxzoz')   # -> "oz"
    # 1. Eliminamos "xx", quedando "zzoz"
    # 2. Eliminamos "zz", quedando "oz"

    remove_snow('abcdd')    # -> "abc"
    # 1. Eliminamos "dd", quedando "abc"

    remove_snow('zzz')      # -> "z"
    # 1. Eliminamos "zz", quedando "z"

    remove_snow('a')        # -> "a"
    # No hay montículos repetidos


if __name__ == "__main__":
    main()
