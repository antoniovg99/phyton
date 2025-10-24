cantidad = float(input("Ingrese la cantidad de dinero depositada: "))
interes = 0.04

ahorro_1 = cantidad * (1 + interes) 
ahorro_2 = cantidad * (1 + interes) ** 2        
ahorro_3 = cantidad * (1 + interes) ** 3


print("El total de ahorros tras el primer año es: ", round (ahorro_1))
print("El total de ahorros tras el segundo año es: ", round (ahorro_2)) 
print("El total de ahorros tras el tercer año es: ", round (ahorro_3))


