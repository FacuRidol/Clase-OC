precios = {
    "manzana":100,
    "banana": 50,
    "naranja":80
}
fruta=input("Ingrese la fruta deseada")
kg=float(input("iNGRESE LOS KG"))
valor= precios.get(fruta) * kg
print(f"El precio total es de {valor}")
