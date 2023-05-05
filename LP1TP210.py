# Crear un programa que solicite dos números al usuario y determine cuál es el
# mayor, y si son iguales mostrar un mensaje.

while(1):
    
    numero1 = int(input("Ingrese el Primer  un numero -> "))
    numero2 = int(input("Ingrese el Segundo un numero -> "))

    if (numero1 > numero2):
        print("El numero mayor es ->", numero1)
    elif (numero2 > numero1):
        print("El numero mayor es ->", numero2)
    else:
        print("Ambos numeros son iguales.")
    print()