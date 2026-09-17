import random
secreto = random.randint(1, 100)
adivinado = False  
print("🤖 He pensado un número del 1 al 100. ¿Puedes adivinarlo?")
while adivinado == False:
    num=int(input("Ingrese su numero"))
    if num==secreto:
        print("Ganaste")
        adivinado=True
    elif num>secreto:
        print("El numero es mas grande que el secreto")
    else:
        print("El numero es mas chico que el secreto")