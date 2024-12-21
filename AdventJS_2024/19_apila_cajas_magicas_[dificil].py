"""
¡Se acerca el día para repartir regalos! Necesitamos apilar los regalos que
transportaremos en el trineo 🛷 y para eso los vamos a meter en cajas 📦.

Los regalos se pueden meter en 4 cajas distintas, donde cada caja soporta 1, 2,
5, 10 de peso y se representan así:
            _
        1: |_|
            _____
        2: |_____|
            _____
        5: |     |
           |_____|
             _________
        10: |         |
            |_________|

Tu misión es que al recibir el peso de los regalos, uses las mínimas cajas
posibles y que, además, las apiles de menos peso (arriba) a más peso (abajo).
Siempre alineadas a la izquierda.

Además, ten en cuenta que al apilarlas, se reusa el borde inferior de la caja.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def distribute_weight(weight: int) -> str:
    # Representaciones de las cajas
    boxRepresentations = {10: [" _________ ", "|         |", "|_________|"],
                          5: [" _____ ", "|     |", "|_____|"],
                          2: [" ___ ", "|___|"],
                          1: [" _ ", "|_|"]}
    # Variable que almacena las cajas ordenadas
    cajas, cajas_ordenadas = [], ""
    # Algoritmo para separar las cajas
    for box in boxRepresentations:
        while weight >= box:
            cajas.append(boxRepresentations[box])
            weight -= box
    # Se guarda una variable con los strings ordenados de las cajas
    temp = ""
    for box in cajas[::-1]:
        for i in range(len(box)-1):
            if temp != "" and i == 0:
                box[i] = temp + box[i][len(temp):]
            cajas_ordenadas += box[i] + "\n"
        temp = box[-1]
    cajas_ordenadas += temp

    return cajas_ordenadas


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    weight = 17
    print(f"\nWeight: {weight}")
    print(distribute_weight(17))
    # Devuelve:
    #  _
    # |_|

    weight = 18
    print(f"\nWeight: {weight}")
    print(distribute_weight(18))
    # Devuelve:
    #  ___
    # |___|


if __name__ == "__main__":
    main()
