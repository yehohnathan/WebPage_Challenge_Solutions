"""
Santa Claus 🎅 está revisando el inventario de su taller para preparar la
entrega de regalos. Los elfos han registrado los juguetes en un array de
objetos, pero la información está un poco desordenada. Necesitas ayudar a Santa
a organizar el inventario.

Recibirás un array de objetos, donde cada objeto representa un juguete y tiene
las propiedades:
- name: el nombre del juguete (string).
- quantity: la cantidad disponible de ese juguete (entero).
- category: la categoría a la que pertenece el juguete (string).

Escribe una función que procese este array y devuelva un objeto que organice
los juguetes de la siguiente manera:
- Las claves del objeto serán las categorías de juguetes.
- Los valores serán objetos que tienen como claves los nombres de los juguetes
y como valores las cantidades totales de cada juguete en esa categoría.
- Si hay juguetes con el mismo nombre en la misma categoría, debes sumar sus
cantidades.
- Si el array está vacío, la función debe devolver un objeto vacío {}.
"""


# ++++++++++++++++++++++++++++++ # FUNCIONES # ++++++++++++++++++++++++++++++ #
def organizeInventory(inventory):
    # Variable que guarda el inventario ordenado en un diccionario
    o_inventory = {}
    # Se accede uno por uno a los diccionarios de la lista "inventory"
    for item in inventory:
        # Se pregunta si ya existe la categoría, sino la crea.
        if item['category'] not in o_inventory:
            o_inventory[item['category']] = {}
        # Se pregunta si el objeto existe en la categoría, sino lo crea
        if item['name'] not in o_inventory[item['category']]:
            o_inventory[item['category']][item['name']] = 0
        # Finalmente le suma la cantidad de objetos que hay
        o_inventory[item['category']][item['name']] += item['quantity']

    return o_inventory


# +++++++++++++++++++++++++++++++++ # MAIN # ++++++++++++++++++++++++++++++++ #
def main():
    inventory = [
        {'name': 'doll', 'quantity': 5, 'category': 'toys'},
        {'name': 'car', 'quantity': 3, 'category': 'toys'},
        {'name': 'ball', 'quantity': 2, 'category': 'sports'},
        {'name': 'car', 'quantity': 2, 'category': 'toys'},
        {'name': 'racket', 'quantity': 4, 'category': 'sports'}]

    print(organizeInventory(inventory))

    inventory2 = [
        {'name': 'book', 'quantity': 10, 'category': 'education'},
        {'name': 'book', 'quantity': 5, 'category': 'education'},
        {'name': 'paint', 'quantity': 3, 'category': 'art'}]

    print(organizeInventory(inventory2))


if __name__ == "__main__":
    main()
