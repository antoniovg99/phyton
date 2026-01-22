asignaturas=["Matmaticas", "Fisica", "Quimica", "Historia", "Lengua"]
notas=[]

for asig in asignaturas:
    nota=input("Que nota has sacado en "+asig+": ")
    notas.append(nota)

for asignaturas, notas in zip(asignaturas, notas):
    print("En ", asignaturas, " has sacado ", notas)

