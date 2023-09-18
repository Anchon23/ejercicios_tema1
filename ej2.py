capital_inicial = 1000
interes_anual = float(input("Ingrese el interés anualentre 1% y 10%: "))
interes = interes_anual/100
print(interes_anual, "%")
calculo =  float(capital_inicial *  (interes+1)**2)
print("El resultado es: ", round(calculo, 2))
