# Crear un programa que solicite un número al usuario y determine si es un
# número de Harshad.

def EsPositivo(numero : str):
    numero = round(float(numero))
    return numero > 0

def EsEntero(numero : str):
    numero = float(numero)
    return (numero % round(numero) == 0)

def CaclularDivisor(numero : str, cantidadDeDigitos):
    divisor = 0
    for i in range (cantidadDeDigitos):
        divisor = divisor + int(numero[i])
    print("Numero Divisor   -> ", divisor)
    return divisor

def CalcularHarshad(numero : str, divisor : int):
    resultado = int(numero) / divisor
    print("Numero Resutado  -> ", resultado)
    return (int(numero) % divisor) == 0 

while(1):

    numero = str(input("Ingrese un numero entero positivo -> "))

    cantidadDeDigitos = len(numero)

    print("Numero Ingresado -> ", numero)
    if(EsEntero(numero) and EsPositivo(numero) and not 0):
        if(CalcularHarshad(numero, CaclularDivisor(numero, cantidadDeDigitos))):
            print("El Numero Ingresado SI ES HARSHAD!!!")
        else:
            print("El Numero Ingresado NO es Harsahd.")
    else:
        print("Ingreso invalido. Ingrese un numero entero positivo.")
    print()
