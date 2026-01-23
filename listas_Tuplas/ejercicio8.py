palabra=input("Introduce una palabra: ")

lista=[]

for letra in palabra:
    lista.append(letra)


n=len(lista)

for i in range(n // 2):
    
    if lista[i] == lista[n-1-i]:
        print("La palabra "+palabra+" es un palindromo")
    else:
        print("La palabra "+palabra+" no es un palindromo")