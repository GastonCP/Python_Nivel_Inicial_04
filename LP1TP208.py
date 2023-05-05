# Crear un programa que solicite un número al usuario y determine si es un
# número par mayor que cero.

def EsNumeroPositivo(numero : int):
    return(numero > 0)

def EsNumeroPar(numero : int):
    return (numero % 2 == 0)

while(1):
    numero = int(input("Ingrese un numero POSITIVO -> "))

    if(EsNumeroPositivo(numero) and EsNumeroPar(numero)):
        print(numero, "-> SI es Par.")
    else:
       print(numero, "-> NO es Par.")
    print()