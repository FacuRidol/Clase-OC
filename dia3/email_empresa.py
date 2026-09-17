def clear_email(nombre, apellido):
    return(f"{nombre}.{apellido}@empresa.com")
nom= input("escriba su nombre")
apelli=input("escriba su apellido")
print(clear_email(nom,apelli))
