def function(ip):
    lista = ip.split(".")
    if len(lista) == 4:
        for i in lista:
            try:
                if int(i) < 0 or int(i) > 255:
                    return False
            except ValueError as e:
                e = "alguno de los valores no es un numero"
                return e
        return True
    else:
        return False

print(function("111.2331.23.12"))
    