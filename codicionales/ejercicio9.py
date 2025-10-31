edad = int(input("Indica su edad: "))
if edad < 4:
    print("La entrada es gratuita")
elif 4 <= edad > 18:
    print("El precio de la entrada es de 5€")
elif edad >= 18:
    print("El precio de la entrada es de 10€")
