# Crear un programa que solicite un número al usuario y determine si es un
# número de dos dígitos.

while(1):
    numero = int(input("Ingrese un numero -> "))

    if((numero > 9) and (numero < 100)) or ((numero < -9) and (numero > -100)):
        print ("El numero ingresado ", numero, ", SI es de 2 digitos")
    else:
        print ("El numero ingresado ", numero, ", NO es de 2 digitos")
    print()
             
             