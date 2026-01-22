numero = int(input("Introduce un numero entero: "))
contador= 0
impares = []
while contador < numero:
    contador = contador + 1
    if contador % 2 != 0:
        impares.append(str(contador))
        
        inversa= map(str, reversed(impares))
        print(inversa)
        

