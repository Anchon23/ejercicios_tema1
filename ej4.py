def calcular_movimientos_validos(num_movimientos):
    # Tabla de movimientos posibles desde cada posición
    movimientos_posibles = {
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
        0: [4, 6]
    }

    # Función para contar movimientos válidos desde una posición dada
    def contar_movimientos_validos(desde, num_movimientos_restantes):
        if num_movimientos_restantes == 0:
            return 1
        else:
            movimientos_validos = 0
            for siguiente_posicion in movimientos_posibles[desde]:
                movimientos_validos += contar_movimientos_validos(siguiente_posicion, num_movimientos_restantes - 1)
            return movimientos_validos

    # Calcular la cantidad total de movimientos válidos
    total_movimientos = 0
    for inicio in range(10):
        total_movimientos += contar_movimientos_validos(inicio, num_movimientos)

    return total_movimientos

# Prueba del algoritmo con diferentes números de movimientos
print("Cantidad de movimientos válidos para 1 movimiento:", calcular_movimientos_validos(1))
print("Cantidad de movimientos válidos para 2 movimientos:", calcular_movimientos_validos(2))
print("Cantidad de movimientos válidos para 3 movimientos:", calcular_movimientos_validos(3))
print("Cantidad de movimientos válidos para 5 movimientos:", calcular_movimientos_validos(5))
print("Cantidad de movimientos válidos para 8 movimientos:", calcular_movimientos_validos(8))
print("Cantidad de movimientos válidos para 10 movimientos:", calcular_movimientos_validos(10))
print("Cantidad de movimientos válidos para 15 movimientos:", calcular_movimientos_validos(15))
print("Cantidad de movimientos válidos para 18 movimientos:", calcular_movimientos_validos(18))
print("Cantidad de movimientos válidos para 21 movimientos:", calcular_movimientos_validos(21))
print("Cantidad de movimientos válidos para 23 movimientos:", calcular_movimientos_validos(23))
print("Cantidad de movimientos válidos para 32 movimientos:", calcular_movimientos_validos(32))