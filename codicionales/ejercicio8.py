puntuacion = float(input("Indica su puntuacion: "))
dinero = int(2400)
if puntuacion == 0.0:
    print("Su nivel de rendimiento es inaceptable")
    print("Su dinero recibido es de: " , dinero, "€")
elif puntuacion == 0.4:
    print("Su nivel de rendimiento es aceptable")
    m = dinero * 0.4
    dinero1 = m + dinero
    print("Su dinero recibido es de: " , dinero1, "€")
elif puntuacion <= 0.6:
    print("Su nivel de rendimiento es meritorio")
    m = dinero * 0.6
    dinero2 = m + dinero
    print("Su dinero recibido es de: " , dinero2, "€")