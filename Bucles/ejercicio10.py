n = int(input("Introduce un numero entero: "))
cont = ""
while cont != "primo":
    n = int(input("Introduce un numero entero: "))
    if n > 2 and n % 2 != 0:
        print (n," es primo")
        cont = "primo"
    
        