cantidad = float(input("Ingrese la cantidad a convertir: "))
interes = float(input("Ingrese el interes anual en porcentaje: "))/ 100
años = int(input("Ingrese la cantidad de años a invertir: "))
capital = cantidad * (1 + interes) ** años
print("El capital tras", años, "años es:", round(capital, 2))

