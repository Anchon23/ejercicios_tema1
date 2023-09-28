cadena_corrupta = "2984 lak ;enrac ed letsap"

nombre_receta = cadena_corrupta.split(";")[1].strip()[::-1]
cantidad_calorias = cadena_corrupta.split(";")[0].strip()[::-1]

cadena_formateada = f"La receta de {nombre_receta} contiene {cantidad_calorias} calorías."

print(cadena_formateada)
