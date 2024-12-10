"""
Los elfos programadores están creando un pequeño ensamblador mágico para
controlar las máquinas del taller de Santa Claus.

Para ayudarles, vamos a implementar un intérprete sencillo que soporte las
siguientes instrucciones mágicas:
- `MOV x y`: Copia el valor x (puede ser un número o el contenido de un
registro) en el registro y
- `INC x`: Incrementa en 1 el contenido del registro x
- `DEC x`: Decrementa en 1 el contenido del registro x
- `JMP x y`: Si el valor del registro x es 0 entonces salta a la instrucción en
el índice y y sigue ejecutándose el programa desde ahí.

Comportamiento esperado:
- Si se intenta acceder, incrementar o decrementar a un registro que no ha sido
inicializado, se tomará el - valor 0 por defecto.
- El salto con JMP es absoluto y lleva al índice exacto indicado por y.
- Al finalizar, el programa debe devolver el contenido del registro A. Si A no
tenía un valor definido, retorna `undefined`.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def compile(instructions):
    # Diccionario de registros
    registros = {}

    # Función para obtener el valor de un operando (número o registro)
    def obtener_valor(operando):
        # lstrip elimina el negativo de los números enteros
        return int(operando) if operando.lstrip(
            '-').isdigit() else registros.get(operando, 0)

    puntero = 0  # Puntero de instrucción
    while puntero < len(instructions):
        partes = instructions[puntero].split()
        # Ejecuta las instrucciones
        if partes[0] == 'MOV':
            registros[partes[2]] = obtener_valor(partes[1])
        elif partes[0] == 'INC':
            registros[partes[1]] = registros.get(partes[1], 0) + 1
        elif partes[0] == 'DEC':
            registros[partes[1]] = registros.get(partes[1], 0) - 1
        elif partes[0] == 'JMP':
            if registros.get(partes[1], 0) == 0:
                puntero = obtener_valor(partes[2]) - 1

        puntero += 1  # Avanza al siguiente comando

    return registros.get('A', 'undefined')


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    instructions = [
       'MOV 0 C',
       'INC A',
    ]   # 1
    print(compile(instructions))

    instructions = [
       'MOV -1 C',     # copia -1 al registro 'C',
       'INC C',        # incrementa el valor del registro 'C'
       'JMP C 1',      # salta a la instrucción en el índice 1 si 'C' es 0
       'MOV C A',      # copia el registro 'C' al registro 'a',
       'INC A'         # incrementa el valor del registro 'a'
    ]   # 2
    print(compile(instructions))

    instructions = [
       'INC A',
       'INC A',
       'DEC A',
       'MOV A B'
    ]   # 1
    print(compile(instructions))

    instructions = [
       'MOV 5 B',
       'DEC B',
       'MOV B A',
       'INC A'
    ]   # 5
    print(compile(instructions))

    instructions = [
       'INC C',
       'DEC B',
       'MOV C Y',
       'INC Y',
    ]   # -undefined
    print(compile(instructions))

    instructions = [
       'MOV 2 X',
       'DEC X',
       'DEC X',
       'JMP X 1',
       'MOV X A'
    ]   # -2
    print(compile(instructions))

    instructions = [
       'MOV 3 C',
       'DEC C',
       'DEC C',
       'DEC C',
       'JMP C 3',
       'MOV C A'
    ]   # -1
    print(compile(instructions))


if __name__ == "__main__":
    main()
