# Crear un programa que solicite dos números al usuario y determine si ambos
# son iguales a cero.

while(1):
    
    numero1 = float(input("Ingrese un primer  numero -> "))
    numero2 = float(input("Ingrese un segundo numero -> "))

    if( numero1 == numero2 == 0):
        print("Ambos numeros ingresados, son iguales a 0")
    else:
        print("Almenso uno de los 2 numeros ingresados son diferentes a 0.")
    print()