# Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.


def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    else:
        inventario.append(item)
        return inventario
    
inventario = ["escopeta", "casco", "chaleco"]
nuevo_item = input("Ingrese el nuevo ítem: ")
agregar_item(inventario, nuevo_item) 
print(inventario)
