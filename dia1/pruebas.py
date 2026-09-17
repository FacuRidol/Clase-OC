try:
    cuenta=float(input("¿Cual es su cuenta?"))
    porcentaje=int(input("¿Cual es el porcentaje?"))
    print(cuenta+cuenta*porcentaje/100)
    print(cuenta*porcentaje/100)
except ValueError:
    print("valores no validos")
    