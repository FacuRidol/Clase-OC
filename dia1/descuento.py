produc=float(input("Ingrese el precio"))
desc=float(input("Ingrese el descuento"))
print(f"El descuento total es {produc * desc/100}")
print(f"El precio total es {produc - produc * desc/100}")