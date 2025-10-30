edad = int(input("Ingrese tu edad: "))
ingreso = int(input("Indica tus ingresos mensuales: "))
if edad > 16 and ingreso >= 1000:
    print("Puedes tributar")
else:
    print("No puedes tributar")
