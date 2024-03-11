numero = input("\n¡Bienvenido, adivinemos el tipo de número!")

#Creamos un ciclo para seguir preguntando
while True:

    # Pedirmos que ingresen un numero
    numero = input("¿En qué número estás pensando? Escribe 'salir' para terminar ")

    # Verificamos si se intrujo salir
    #numero.lower lo utilizamos para reconocer si se escribio salir ya sea minuscula o mayuscula
    if numero.lower() == 'salir':
        print("\n¡Hasta la próximaaa!")
        break

    try:
        # Convertimos la entrada a entero
        numero = int(numero)

        # Verificamos si el número está en el rango permitido
        if 1 <= numero <= 1000:
            # Comprobamos si el número es par o impar
            if numero % 2 == 0:
                print(f"\n¡El número {numero} es par! ¿Quieres probar con otro?")
            else:
                print(f"\n¡El número {numero} es impar! ¿Quieres probar con otro?")
        else:
            print("\nIngresa un número entre 1 y 1000")
    except ValueError:
        print("\nIngresa un número o escribe 'salir'")