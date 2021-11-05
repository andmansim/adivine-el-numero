"""
Ejerercicio: hacer un juego "Guess The number"

Parte 1: Pedir al usuario que introduzca un número entre 0 y 100
Parte 2: Adivinar el número por parte del usuario

"""
# Parte 1

# Para el ejercicio del primer capítulo, hay que utilizar lo que sigue:
# import random
# numero = random.randint(0,100)

# Para resaltar el segundo capítulo, hay que utilicar lo que sigue:
print("Introduzca el numero a adivinar")

while True:
    # Entramos en un bucle infinito

    # Pedimos introducir un numero
    numero = input("Introduzca un numero entre 0 y 99 incluidos: ")

    try:
        numero = int(numero)
    except:
        pass
    else:
        #Hacer la comparación
        if 0 <= numero <= 99:
            # Tenemos lo que queremos, salimos del bucle 
            break
            
# Parte 2
print("intente encontrar el numero a adivinar")
while True: #Bucle 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos
    
    while True: # Bucle 2
        # Entregamos en un bucle infinito
        # que permite corregir un error de escritura

        # Pedimos introducir un número
        intento = input("Introduzca un numero entre 0 y 99 incluidos: ")

        try:
            intento = int(intento)
        except: 
            pass
        else: 
            # Hacer la comparación
            if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del Bucle 2 
                break
    
    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento < numero:
        print("Demasiado grande")
    else: 
        print("Victoria!")
        # Terminamos la partida, salimos del Bucle 1 break

