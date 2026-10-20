par=[]
impar=[]
a=0
while a==0:
    try:
        ing=float(input("Ingrese un valor"))
        if ing%2==0:
            par.append(ing)
        else:
            impar.append(ing)
    except ValueError:
        print(f"Los pares son {par}")
        print(f"Los impares son {impar}")