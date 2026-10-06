nom=["Facu","Rosset","Sainz","Ridolfi"]
notas=[10,2,5,8]
anio=["primero","segundo","tercero","cuarto","quinto","sexto"]
edad=[16,15,15,14]
cant=int(input("Ingrese la cantidad de alumnos que quiera mostrar menor a 5 "))
if cant<5:
    for i in range(cant):
        print(nom[i])
        print(f"Su nota es: {notas[i]}")
        if edad[i]>15:
            print(f"Su curso es: {anio[2]}")
        elif edad[i]>14:
            print(f"Su curso es: {anio[1]}")
        else:
            print(f"Su curso es: {anio[0]}")

ing=int(input("Ingrese la id del estudiante "))
if ing<4:
    print(nom[ing])
    print(f"Su nota es: {notas[ing]}")
    if edad[ing]>15:
        print(f"Su curso es: {anio[2]}")
    elif edad[ing]>14:
        print(f"Su curso es: {anio[1]}")
    else:
        print(f"Su curso es: {anio[0]}")    

