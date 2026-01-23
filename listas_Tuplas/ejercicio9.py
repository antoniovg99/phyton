palabra=input("Introduce una palabra: ")

vocales=["a", "e", "i", "o", "u"]

lista=[]

for letra in palabra:
    lista.append(letra)

    

for v in vocales:
    contador=0
    for vl in lista:
        if vl == v:
            contador=contador+1
    print("La vocal "+v+" aparece "+str(contador)+" veces")
    




