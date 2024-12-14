"""
¡El grinch 👹 ha pasado por el taller de Santa Claus! Y menudo desastre ha
montado. Ha cambiado el orden de algunos paquetes, por lo que los envíos no se
pueden realizar.

Por suerte, el elfo Pheralb ha detectado el patrón que ha seguido el grinch
para desordenarlos. Nos ha escrito las reglas que debemos seguir para reordenar
los paquetes. Las instrucciones que siguen son:
- Recibirás un string que contiene letras y paréntesis.
- Cada vez que encuentres un par de paréntesis, debes voltear el contenido
dentro de ellos.
- Si hay paréntesis anidados, resuelve primero los más internos.
- Devuelve el string resultante con los paréntesis eliminados, pero con el
contenido volteado correctamente.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
# La idea es hacer una función recursiva. Los paréstesis anidados se pueden ver
# como paquetes dentro de paquetes
def fix_packages_recurrencia(packages):
    # Convertir el string en una lista para manipular caracteres
    # individualmente
    packages = list(packages)

    i = 0  # Inicializar el índice para recorrer la lista
    # Ciclo para procesar cada carácter en la lista
    while i < len(packages):
        if packages[i] == "(":
            # Eliminar el paréntesis "(" del paquete actual
            packages.pop(i)
            # Procesar recursivamente el contenido después del paréntesis "("
            # y reemplazarlo con su versión procesada
            packages[i:] = fix_packages_recurrencia(packages[i:])
        elif packages[i] == ")":
            # Invertir los caracteres antes del paréntesis de cierre ")"
            packages[:i] = ''.join(reversed(packages[:i]))
            packages.pop(i)     # Eliminar el paréntesis de cierre ")"
            return packages
        i += 1      # Continuar al siguiente carácter

    return ''.join(packages)


# Usando expresiones regulares, se encuentra el inidice inicial y final, luego
# se le da vuelta al contenido. Esta solución contempla los paréstesis
# desbalanceados.
def fix_packages(packages):
    while "(" in packages:  # Continuar mientras haya paréntesis en el string
        # Encontrar el paréntesis más interno usando rfind (última apertura)
        start = packages.rfind("(")
        # Buscar el primer paréntesis de cierre después del más interno
        end = packages.find(")", start)

        if end == -1:  # Si no se encuentra un paréntesis de cierre, omitirlo
            packages = packages[:start] + packages[start + 1:]
            continue

        # Extraer el contenido entre los paréntesis
        inner = packages[start + 1:end]
        # Invertir el contenido y reemplazarlo en el string original
        packages = packages[:start] + inner[::-1] + packages[end + 1:]

    # Si quedan paréntesis de cierre desbalanceados, eliminarlos
    packages = packages.replace(")", "")

    return packages


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    print(fix_packages('a(bc)de'))              # ➞ "acbde"

    print(fix_packages('a(bc(def)g)h'))         # ➞ "agdefcbh"

    print(fix_packages('abc(def(gh)i)jk'))      # ➞ "abcighfedjk"

    print(fix_packages("(abc(def(ghi)))"))      # ➞ "defihgcba"


if __name__ == "__main__":
    main()
