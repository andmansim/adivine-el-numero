import random
numero = random.randint(0,100)
print(numero)
print("Intento es un numero entero")
intento_1 = int(input())

while intento_1 != numero:
    
    if intento_1 > 99:
        print("Choose another number between 0 an 99")
    else:
        if intento_1 > numero:
            print("Te has pasado un poco. El numero esta entre:" + "0 y" + str(intento_1))
        else:
            print("Te has quedado corto. El numero esta entre:" + str(intento_1) + "y 99")
    intento_1 = int(input())
if intento_1 == numero:
     print("¡Congratulations!")