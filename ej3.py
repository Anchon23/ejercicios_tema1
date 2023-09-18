lista_1 = ['amazon','google','meta','apple','microsoft']
lista_2 = ['tesla','telefonica','apple','microsoft','google']
lista_3 = lista_1 + lista_2
lista_4 = []
for i in lista_3:
    if i not in lista_4:
        lista_4.append(i)
print(lista_4)