
num1= float(input("Ingrese el dividendo de la division"))
while True:
    try:
        num2= float(input("Ingrese el divisor de la division"))
        print(num1/num2)
        break
    except ZeroDivisionError:
        print("no se divide por 0")
        
