"""
Estás en un mercado muy especial en el que se venden árboles de Navidad 🎄.
Cada uno viene decorado con una serie de adornos muy peculiares, y el precio
del árbol se determina en función de los adornos que tiene.

- *: Copo de nieve - Valor: 1
- o: Bola de Navidad - Valor: 5
- ^: Arbolito decorativo - Valor: 10
- #: Guirnalda brillante - Valor: 50
- @: Estrella polar - Valor: 100

Normalmente se sumarían todos los valores de los adornos y ya está…

Pero, ¡ojo! Si un adorno se encuentra inmediatamente a la izquierda de otro de
mayor valor, en lugar de sumar, se resta su valor.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def calculate_price(ornaments: str) -> int:
    adornos = {'*': 1, 'o': 5, '^': 10, '#': 50, '@': 100}

    # Variable que almacena el resultado
    resultado = 0
    # Almacena el valor previo (comienza en cero por ser menor que 1)
    prev_value = 0

    for char in ornaments:
        # Verifica que no se encuentre ningun valor no deseado
        if char not in adornos:
            return

        # Almacena el valor actual
        current_value = adornos[char]
        # Verifica que el valor previo sea menor que el actual, y se resta
        # doble
        if prev_value < current_value:
            # Como siempre se va sumando el valor actual, si se detecta que
            # dicho valor (ahora el previo) es menor que el nuevo valor actual
            # se resta multiplicando por dos para que actue como si fuese una
            # simple resta
            resultado -= prev_value * 2
        # Suma siempre el valor actual a resultado
        resultado += current_value
        # Nuevo valor previo, igual al valor actual
        prev_value = current_value
    return resultado


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    calculate_price('***')      # 3   (1 + 1 + 1)
    calculate_price('*o')       # 4   (5 - 1)
    calculate_price('o*')       # 6   (5 + 1)
    calculate_price('*o*')      # 5  (-1 + 5 + 1)
    calculate_price('**o*')     # 6  (1 - 1 + 5 + 1)
    calculate_price('o***')     # 8   (5 + 3)
    calculate_price('*o@')      # 94  (-5 - 1 + 100)
    calculate_price('*#')       # 49  (-1 + 50)
    calculate_price('@@@')      # 300 (100 + 100 + 100)
    calculate_price('#@')       # 50  (-50 + 100)
    calculate_price('#@Z')      # undefined (Z es desconocido)


if __name__ == "__main__":
    main()
