numeros=[]

for i in range(10):
    n=input("Introduce numeros del 1 al 10: ")
    numeros.append(n)

numeros.sort(reverse=True)
resultado=", ".join(numeros)

print(resultado)