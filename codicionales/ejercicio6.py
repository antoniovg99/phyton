nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (M/F): ")
primeraLetra = nombre[0]
if sexo == "F" and primeraLetra > "M":
    print ("Correspondes al grupo A")
elif sexo == "M" and primeraLetra < "N":
    print ("Correspondes al grupo A")
else:
    print ("Correspondes al grupo B")
 