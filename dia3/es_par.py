def es_par(num):
    if num%2==0:
        return True
    else:
        return False
numero=int(input("Ingrese su numero"))
estado=es_par(numero)
print(f"Es par?{estado}")
