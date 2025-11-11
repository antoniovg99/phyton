cantidad = int(input("Introduce la cantidad a invertir: "))
interes = int(input("Introduce el interes anual: "))
años = int(input("Introduce el numero de años :"))
cont = int(1)
while cont <= años:
    interes2 = interes / 100
    calculo =  1+interes2
    calculo2 = calculo * cont
    capital= calculo2 * cantidad
    cont = cont + 1
    print ("El captial obtenido el año ",cont," es de :",capital)
