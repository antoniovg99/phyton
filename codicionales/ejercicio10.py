tipoPizza= input("Indica si quieres que la pizza sea Vegetariana(SI o NO): ")
if tipoPizza == "SI" :
    print ("Las pizzas vegetarianas llevan mozzarella y tomate, a parte del ingrediente a elegir: ")
    ingrediente = input ("De los siguientes ingredientes seleccione 1: pimiento y tofu: ")
    print ("Su pizza vegetariana lleva mozzarella, tomate y " , ingrediente)

elif tipoPizza == "NO" :
    print ("Las pizzas no vegetarianas llevan mozzarella y tomate, a parte del ingrediente a elegir: ")
    ingrediente = input ("De los siguientes ingredientes seleccione 1: peperoni, jamon y salmon: ")
    print ("Su pizza no vegetariana lleva mozzarella, tomate y " , ingrediente)
