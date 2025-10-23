precio = float(input("Introduce el precio del producto: "))
print (f"El precio del prodcuto es:  {precio:.2f} €")
precio_str = f"{precio:.2f}"
cantidad = precio_str.split(".")
euros = cantidad[0]
centimos = cantidad[1]
print ("Euros: ", euros, "Centimos: ", centimos)