palabra = (input("Introduce una palabra: "))

invertido = reversed(palabra)#invierte el orden de la palabra "hola" => "aloh"

for letra in invertido: #muestra letra por letra la palabra invertida
    print(letra)
