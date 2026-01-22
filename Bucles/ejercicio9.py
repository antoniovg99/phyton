contraseña = "contraseña"
pas = (input("Introduce la contraseña: "))

while contraseña != pas :
    pas = (input("Introduce la contraseña: "))
    if pas == contraseña:
        contraseña = pas
        print("Contraseña correcta")
    