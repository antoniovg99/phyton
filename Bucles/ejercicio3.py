numero = int(input("Introdce un numero: "))
contador = int(0)
impar = []
while contador <= numero:
    contador = contador + 1
    if contador % 2 != 0:
        impar.append(str(contador)) #para convertir un nmero entero en una cadena de texto en un array
        resltado = ",".join(impar) #une las comas con el contenido del array
        
print (resltado)
