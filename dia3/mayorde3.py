numeros=3
def mayorde3(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return (n1)
        else:
            return(n3)
    else:
        if n2>n3:
            return(n2)
n1=int(input("Ingrese un numero"))
n2=int(input("Ingrese un numero"))
n3=int(input("Ingrese un numero"))
print (mayorde3(n1,n2,n3))
