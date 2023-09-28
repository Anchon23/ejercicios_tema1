def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    else:
        inventario.append(item)
        return inventario
    
inventario = ["escopeta", "casco", "chaleco"]
nuevo_item = input("Ingrese un nuevo ítem: ")
agregar_item(inventario, nuevo_item) 
print(inventario)