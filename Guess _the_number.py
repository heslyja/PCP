# El módulo random se utiliza para generar selecciones aleatorias
import random
# Creamos la función que contendrá la lógica
def adivina():
    # Generamos un número aleatorio entre 1 y 50
    secreto = random.randint(1, 50)
    # Inicializamos una variable en 0 para llevar la cuenta de intentos
    intentos = 0
    # Este bucle seguirá ejecutándose hasta que el usuario adivine el número o decida dejar de jugar
    while True:
        # Utilizamos un bloque try por si el usuario no ingresa un número
        try:
            # Usuario ingresa un número y convertimos a entero, si usuario no ingresa número será error
            eleccion = int(input("\nAdivina un número entre 1 y 50: "))
            # Verificamos que la elección esté dentro del rango permitido 
            if 1 <= eleccion <= 50:
                # Si está dentro del rango, incrementamos el contador de intentos
                intentos += 1
                # Comprobamos si la elección coincide con el número secreto
                if eleccion == secreto:
                    # Si el usuario acierta, felicitamos al usuario, mostramos el número de intentos 
                    print(f"\n¡Felicidades, ganaste! {secreto}")
                    print(f"Número de intentos: {intentos}")
                    #Termina el bucle si se cumple esta condición
                    break
                else:
                    # Si el usuario no acierta, preguntamos si quiere seguir jugando y convertimos a minúscula
                    seguir = input("Incorrecto. ¿Quieres seguir jugando? (s/n): ").lower()
                    # Si indica que seguirá jugando 's', se continua
                    if seguir == 's':
                        print("¡Genial! Continuemos jugando.")
                    # Si indica que no seguirá jugando 'n', mostramos el número secreto, el número de intentos y salimos del bucle con un break
                    elif seguir == 'n':
                        print(f"\nEl número secreto era: {secreto}")
                        print(f"Número de intentos: {intentos}")
                        print("¡Hasta la próxima!")
                        break
                    # Si indica una letra que no sea una de las opciones, dará error
                    else:
                        print("No se reconoce la entrada. Por favor, escribe 's' para continuar o 'n' para salir.")
            # Si el número no está dentro del rango, pedimos que lo intente de nuevo
            else:
                print("Intenta de nuevo, elige un número dentro del rango de 1 a 50.")
        # Error por no ingresa un número
        except ValueError:
            print("Error")
# Llamamos a la función para iniciar el juego
adivina()
