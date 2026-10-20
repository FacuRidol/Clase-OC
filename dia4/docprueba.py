# Variables Globales
saldo = 1000
pin="hola"
# 1. Definir funciones
def verificar_pin(pin_usuario):
    # Tu código aquí (return True o False)
    if pin_usuario==pin:
        return True
    else:
        return False
    pass

def retirar(monto):
    global saldo # Necesario para modificar la variable de afuera
    # Tu código aquí (if monto > saldo...)
    if monto>saldo:
        print("saldo insuficiente")
    else:
        saldo=saldo-monto
    pass

# 2. Ejecución Principal
print("🏦 Bienvenido al Banco Python")

input_pin = input("Ingrese su PIN: ")

if verificar_pin(input_pin)==True:
    print("Acceso concedido. Saldo actual:", saldo)
    
    try:
        monto_str = input("¿Cuánto desea retirar? ")
        monto = int(monto_str)
        retirar(monto)
        print("su saldo restante son : ", saldo)
        
        # Llamar a la función de retirar
        
    except ValueError:
        print("Error: Ingrese un número válido.")
else:
    print("PIN Incorrecto. Policía en camino.")