import random
numero = random.randint(0,100)
print(numero)
print("Intento es un numero entero")
intento_1 = input()

while str(intento_1) != str(numero):
    
    if str(intento_1) > str(99):
        print("Choose another number between 0 an 99")
    else:
        if str(intento_1) > str(numero):
            print("Te has pasado un poco. El numero esta entre:" + "0 y" + str(intento_1))
        else:
        #if str(intento_1) < str(numero):
            print("Te has quedado corto. El numero esta entre:" + str(intento_1) + "y 99")
    intento_1 = input()
if str(intento_1) == str(numero):
     print("¡Congratulations!")