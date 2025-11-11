n = int(input("Introduce un numero entero: "))
cont = 0
impares = []
while cont <= n:
    if cont % 2 != 0:
        impares.append(str(cont)) #para convertir un nmero entero en una cadena de texto en un array
        invertido = map(str, reversed(impares)) #muestra el array del reves
        result = " ".join(invertido)
        print (result)
    cont = cont +1