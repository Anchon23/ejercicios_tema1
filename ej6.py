def clasificar_personajes(personajes):
    humanos = []
    no_humanos = []

    for personaje in personajes:
        if personaje.get("es_humano", False):
            humanos.append(personaje)
        else:
            no_humanos.append(personaje)

    humanos = sorted(humanos, key=lambda x: x["nombre"])
    no_humanos = sorted(no_humanos, key=lambda x: x["nombre"])

    return humanos, no_humanos

personajes = [
    {"nombre": "Arthur Morgan", "es_humano": True},
    {"nombre": "Sonic", "es_humano": False},
    {"nombre": "Deacon", "es_humano": True},
    {"nombre": "Donkey Kong", "es_humano": False},
    {"nombre": "Pikachu", "es_humano": False},
]

humanos, no_humanos = clasificar_personajes(personajes)

print("Personajes humanos:")
for personaje in humanos:
    print(personaje["nombre"])

print("\nPersonajes no humanos:")
for personaje in no_humanos:
    print(personaje["nombre"])
