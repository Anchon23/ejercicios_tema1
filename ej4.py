def function(ip):
    lista = ip.split(".")
    if len(lista) == 4:
        for i in lista:
            try:
                int(i) < 0 or int(i) > 255
                return False
            except ValueError as e:
                e = "alguno de los valores no es un numero"
                return e
        return True
    else:
        return False

print(function("192.188.1.38"))
    