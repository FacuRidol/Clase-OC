prog=  "piedra"
u= str(input("Elige entre piedra papel o tijera"))
if u==prog:
    print("Empate")
elif u=="papel":
    print("Ganaste")
elif u=="tijera":
    print("Perdiste")
else:
    print("ERRor")