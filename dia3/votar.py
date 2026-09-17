def puede_votar(edad):
    if edad>=18:
        return ("Puede votar")
    else:
        return ("No puede votar")
print(puede_votar(int(input("escriba su edad"))))