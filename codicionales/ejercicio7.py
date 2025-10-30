rentaAnual = int(input("Ingrese su renta anual: "))
if rentaAnual < 10000:
    print ("Tiene un tipo de impositivo de 5%")
elif rentaAnual > 10000 and rentaAnual < 20000:
    print ("Tiene un tipo de impositivo de 15%")
elif rentaAnual > 20000 and rentaAnual < 35000:
    print ("Tiene un tipo de impositivo de 20%")
elif rentaAnual > 35000 and rentaAnual < 60000:
    print ("Tiene un tipo de impositivo de 30%")
elif rentaAnual > 60000:
    print ("Tiene un tipo de impositivo de 45%")