# Crear un programa que solicite dos números al usuario y determine si el
# segundo número es divisor del primero.

def EsEnteroDe2Digitos(numero : int):
    return (numero > 9) and (numero < 100)
    
def EsEnteroPositivo(numero : int):
    return(numero > 0)

while(1):    
    numero = int(input("Ingrese un numero -> "))
    decena = round(numero/10)
    unidad = numero - (decena*10)

    if(EsEnteroPositivo(numero) and EsEnteroDe2Digitos(numero) ):
        
        if(unidad == 0):
            print("El segundo numero NO es divisor de primero.")
        elif(decena % unidad == 0):
            print("El segundo numero SI es divisor de primero.")
        else:
            print("El segundo numero NO es divisor de primero.")
    else:
        print("Ingrese un numero positivo de 2 digitos.")
    print()

