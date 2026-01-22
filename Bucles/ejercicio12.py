frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

cont = 0

for letras in frase:
    if letras == letra:
        cont = cont + 1

print ("La letra ",letra," se repite en la frase ",frase," ",cont," veces")