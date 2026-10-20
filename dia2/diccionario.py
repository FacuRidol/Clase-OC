import time
verduras=["zanahoria","papa","cebolla","remolacha"]
verdu=verduras.copy()
hola=int(input("Ingrese la id del producto"))
print(verdu[hola])
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
nomb=["facu","rosset","sainz","pablo","pedro","valen","zuchi","nacho","marques","barry"]
time.sleep(1)
for i in range(10): 
    hola1=int(input("Ingrese un numero"))  
    abcd= {
        "a":10,
        "b":nomb[i],
        "c":list[hola1]
    }
    variable=abcd.get("c")
    variable1=abcd.get("b")
    print(variable)
    print(variable1)
    time.sleep(0.25)
print("Finalizado")


