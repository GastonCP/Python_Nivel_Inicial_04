# .Crear un programa que solicite un número al usuario y determine si es
# múltiplo de 3

def EsMultiploDe3(numero : int):
    return (numero % 3 == 0)
    
while(1):
    
    numero = int(input("Ingrese un numero entero y positivo -> "))

    if(EsMultiploDe3(numero)):
        print("El numero ingresado", numero,", SI es multiplo de 3.")
    else:
        print("El numero ingresado", numero,", NO es multiplo de 3.")
    print()