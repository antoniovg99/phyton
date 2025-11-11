n = int(input("Introduce un numero: "))
cont = int(n)
numeros = []
while cont >= 0 :
    numeros.append(str(cont))
    resultado = ",".join(numeros) 
    cont= cont -1
    
print (resultado)