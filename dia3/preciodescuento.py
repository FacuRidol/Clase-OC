def calcular_precio_final(pr,ds):
    return (pr-(pr*(ds/100)))
print(calcular_precio_final(int(input("precio:")),int(input("descuento:"))))
