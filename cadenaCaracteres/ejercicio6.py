frase = input ("Introduce una frase: ")
vocal = input ("Introduce una vocal: ").lower()
fraseModificada = frase.replace(vocal, vocal.upper())
print (fraseModificada)