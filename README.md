# adivine-el-numero

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/andmansim/adivine-el-numero.git)
https://github.com/andmansim/adivine-el-numero.git

Hemos resuelto un juego de adivinar un número entero entre el 0 y el 100.
El diagrama de flujo que tenemos en nuestro código es el siguiente:

![diagrama de flujo adivine el número](andmansim/adivine-el-numero/figma-juego-de-adivinar-el-numero.jpg)

```import random
numero = random.randint(0,100)
print(numero)
print("Intento is an integer")
intento_1 = int(input())

while intento_1 != numero:
    
    if intento_1 > 99:
        print("Choose another number between 0 an 99")
    else:
        if intento_1 > numero:
            print("Too far from the number, it's smaller. The number is between:" + "0 y" + str(intento_1))
        else:
            print("Too far from the number, it's bigger. The number is between:" + str(intento_1) + "y 99")
    intento_1 = int(input())
if intento_1 == numero:
     print("¡Congratulations!")
