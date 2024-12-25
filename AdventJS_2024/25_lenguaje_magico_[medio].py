"""
¡Ya hemos repartido todos los regalos! De vuelta al taller, ya comienzan los
preparativos para el año que viene.

Un elfo genio está creando un lenguaje de programación mágico 🪄, que ayudará
a simplificar la entrega de regalos a los niños en 2025.

Los programas siempre empiezan con el valor 0 y el lenguaje es una cadena de
texto donde cada caracter representa una instrucción:
- `>` Se mueve a la siguiente instrucción
- `+` Incrementa en 1 el valor actual
- `-` Decrementa en 1 el valor actual
- `[` y `]`: Bucle. Si el valor actual es 0, salta a la instrucción después
de `]`.  Si no es 0, vuelve a la instrucción después de `[`.
- `{` y `}`: Condicional. Si el valor actual es 0, salta a la instrucción
después de `}`. Si no es 0, sigue a la instrucción después de `{`.

Tienes que devolver el valor del programa tras ejecutar todas las
instrucciones.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def execute(code: str) -> int:
    # Guarda el resultado de todos las operaciones
    resultado = 0
    # Condicionales especiales para {} y []
    corchetes, cuadrado = False, False
    # Lee todas las instrucciones
    i = 0
    while i < len(code):
        char = code[i]

        # Condicionales especiales para bucles y condicionales
        if not corchetes and not cuadrado:
            if char == '+':
                resultado += 1
            elif char == '-':
                resultado -= 1

        # Acciona la instrucción de bucle o condicional
        if char == '{' and resultado == 0:
            corchetes = True
        elif char == '}':
            corchetes = False
        elif char == '[':
            resultado = 0
            cuadrado = True
        elif char == ']':
            cuadrado = False

        i += 1

    return resultado


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print("\n+++++++++++++++++++++++ TEST 1 +++++++++++++++++++++++")
    print(type(execute('+++')))             # int
    print("\n+++++++++++++++++++++++ TEST 2 +++++++++++++++++++++++")
    print(execute('+++'))                   # 3
    print("\n+++++++++++++++++++++++ TEST 3 +++++++++++++++++++++++")
    print(execute('+--'))                   # -1
    print("\n+++++++++++++++++++++++ TEST 4 +++++++++++++++++++++++")
    print(execute('>+++[-]'))               # 0
    print("\n+++++++++++++++++++++++ TEST 5 +++++++++++++++++++++++")
    print(execute('>>>+{++}'))              # 3
    print("\n+++++++++++++++++++++++ TEST 6 +++++++++++++++++++++++")
    print(execute('+{[-]+}'))               # 1
    print("\n+++++++++++++++++++++++ TEST 7 +++++++++++++++++++++++")
    print(execute('-[+>]++'))               # 2
    print("\n+++++++++++++++++++++++ TEST 8 +++++++++++++++++++++++")
    print(execute('-[+{++}]++{[-]}++'))     # 2
    print("\n+++++++++++++++++++++++ TEST 9 +++++++++++++++++++++++")
    print(execute('{+}{+}{+}'))             # 5
    print("\n+++++++++++++++++++++++ TEST 10 +++++++++++++++++++++++")
    print(execute(''))                      # 0
    print("\n+++++++++++++++++++++++ TEST 11 +++++++++++++++++++++++")
    print(execute('+++{[-]+++[-]+}'))       # 1
    print("\n+++++++++++++++++++++++ TEST 12 +++++++++++++++++++++++")
    print(execute('{>++>++}'))              # 0
    print("\n+++++++++++++++++++++++ TEST 13+++++++++++++++++++++++")
    print(execute('++++[-->]>++'))          # 2


if __name__ == "__main__":
    main()
