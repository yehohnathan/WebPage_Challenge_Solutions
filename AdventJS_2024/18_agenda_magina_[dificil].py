"""
Santa Claus tiene una agenda mágica 📇 donde guarda las direcciones de los
niños para entregar los regalos. El problema: la información de la agenda está
mezclada y malformateada. Las líneas contienen un número de teléfono mágico,
el nombre de un niño y su dirección, pero todo está rodeado de caracteres
extraños.

Santa necesita tu ayuda para encontrar información específica de la agenda.
Escribe una función que, dado el contenido de la agenda y un número de
teléfono, devuelva el nombre del niño y su dirección.

Ten en cuenta que en la agenda:
- Los números de teléfono están formateados como +X-YYY-YYY-YYY (donde X es uno
o dos dígitos, e Y es un dígito).
- El nombre de cada niño está siempre entre < y >

La idea es que escribas una funcióna que, pasándole el teléfono completo o una
parte, devuelva el nombre y dirección del niño. Si no encuentra nada o hay más
de un resultado, debes devolver null.
"""
import re


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def find_in_agenda(agenda: str, phone: str) -> dict | None:
    # La agenda pasa a ser una lista
    agenda = agenda.split("\n")

    # Creo un diccionario del mismo tamaño que las ocurrencias de teléfonos
    only_one = [info for info in agenda if phone in info]
    # Se el tamaño de only_one es 1, se retorna el nombre y la dirección
    if len(only_one) == 1:
        only_one[0] = re.sub(
            r'\+\d{1,2}-\d{3,4}-\d{3,4}-\d{3,4}', '', only_one[0])
        name = re.findall(r'<(.+)>', only_one[0])
        only_one = only_one[0].replace(f'<{name[0]}>', '')
        return {'name': name[0], 'address': only_one.strip()}

    # Si no es 1, el tamaño de only_one, se retorna none
    return None


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    # Ejemplo de uso
    agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""

    print(find_in_agenda(agenda, '34-600-123-456'))
    #   { name: "Juan Perez", address: "Calle Gran Via 12" }

    print(find_in_agenda(agenda, '600-987'))
    #   { name: "Maria Gomez", address: "Plaza Mayor 45 Madrid 28013" }

    print(find_in_agenda(agenda, '111'))
    #   null
    #   Explicación: No hay resultados

    print(find_in_agenda(agenda, '1'))
    #   null
    #   Explicación: Demasiados resultados


if __name__ == "__main__":
    main()
