# Crear un programa que solicite dos números al usuario y determine si ambos
# son positivos o negativos

def EsPositivo(numero : float):
    return numero > 0

while(1):

    numero1 = float(input("Ingrese un primer  numero  -> "))
    numero2 = float(input("Ingrese un segundo numero  -> "))

    if(numero1 == 0 or numero2 == 0):
        print("Almenos uno de los numeros ingresados es 0.")
    elif(EsPositivo(numero1) and EsPositivo(numero2)):
        print ("Ambos numeros ingresados son positivos.")
    elif(not(EsPositivo(numero1)) and not(EsPositivo(numero2))):
        print ("Ambos numeros ingresados son negativos.")
    else:
        print("Los numeros ingresados tienen distinto signo.")
    print()