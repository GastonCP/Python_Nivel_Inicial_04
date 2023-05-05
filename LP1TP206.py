# Crear un programa que solicite un número al usuario y determine si es un
# número primo.

while(1):
    numero = int(input("Ingrese un numero -> "))

    contador = 0
    indice = numero

    while (indice > 0):
        if(numero % indice == 0):
            contador = contador + 1
        indice = indice - 1

    if (contador == 2):
        print(numero, "-> SI es numero Primo")
    else:
        print(numero, "-> NO es numero primo. tiene ", contador, " divisores.")
    print()   
