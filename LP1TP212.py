# Crear un programa que solicite un número al usuario y determine si es un
# número triangular

def EsTriangular(numero : int):
    indice = 1
    contador = 1
    while(indice < numero):
        indice = indice + (contador + 1)
        contador = contador + 1
    return indice == numero
    
while(1):
    
    numero = int(input("Ingrese un numero entero y positivo -> "))

    if(EsTriangular(numero)):
        print("El numero ingresado",numero ,"SI es triangular.")
    else:
        print("El numero ingresado",numero ,"NO es triangular.")
    print()