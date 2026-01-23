precios=[50, 75, 46, 22, 80, 65, 8]

mayor=precios[0]
menor=precios[0]
for n in precios:
    if n > mayor:
        mayor=n
    if n < menor:
        menor=n
print("El numero mayor es: "+str(mayor))
print("El numero menor es: "+str(menor))
        