asignaturas=["Matmaticas", "Fisica", "Quimica", "Historia", "Lengua"]
suspensas=["Matmaticas", "Fisica", "Quimica", "Historia", "Lengua"]


for asig in asignaturas:
    nota=input("Intrduzca las notas de cada asignatura " +asig+": ")
    if nota > "4":
        suspensas.remove(asig)
    
print(suspensas)
    

