misiones = [
    (1, "Colter"),
    (3, "Mirador de herradura"),
    (2, "Clemens Point"),
    (4, "Saint denis"),
    (2, "Guarma"),
    (5, "Beaver Hollow"),
    (3, "Beecher's Hope")
]

misiones_ordenadas = sorted(misiones, key=lambda x: x[0])

nombres_misiones = [nombre for _, nombre in misiones_ordenadas]

for nombre in nombres_misiones:
    # Las misiones estan ordenadas de menor a mayor dificultad
    print(nombre)
