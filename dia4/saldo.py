saldo=1000
pin="1234"
def pin_v (pin_ing):
    if pin_ing == pin:
        return True
    else:
        return False
def retirar (cant):
    global saldo
    if cant>saldo:
        print("Fondos insuficientes")
    else:
        saldo=saldo-cant
        print("Transaccion exitosa")
        
while True:
    pin_i=input("Ingrese su pin")
    if pin_v (pin_i)== True:
        while True:
            try:
                can=float(input("Ingrese el saldo a retirar"))
                retirar(can)
                print("Su saldo restante es de" , saldo)
                break
            except ValueError:
                print("Monto no numerico")
        break
    else:
        print("Pin incorrecto, ingreselo nuevamente")




