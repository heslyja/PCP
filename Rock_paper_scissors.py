# Definimos la función 
def escoge_usuario():
    # Pedimos que ingrese la elección y la convertimos a minúscula
    opcion = input("Usuario 1: elige piedra, papel o tijera: ").lower()
    # Creamos un blucle que verifica si la elección del usuario es válida
    while opcion not in ["piedra", "papel", "tijera"]:
        opcion = input("Error").lower()
    return opcion

# Repetimos para usuario 2
def escoge_usuario2():
    opcion2 = input("\nUsuario 2: elige piedra, papel o tijera: ").lower()
    while opcion2 not in ["piedra", "papel", "tijera"]:
        opcion2 = input("Error").lower()
    return opcion2

# Definimos la función para determinar el ganador del juego basado en las elecciones de los usuarios
def ganador(usuario, usuario2):
    # Si ambas elecciones son iguales, se declara un empate
    if usuario == usuario2:
        return "Empate"
    # Estas líneas determinan si el usuario ha ganado según las reglas del juego
    elif (usuario == "piedra" and usuario2 == "tijera") or \
         (usuario == "papel" and usuario2 == "piedra") or \
         (usuario == "tijera" and usuario2 == "papel"):
        return "ganaste"
    # Si no se cumple ninguna de las condiciones anteriores, significa que Usuario 1 perdió
    else:
        return "perdiste"

# Creamos función para jugar
def jugar():
    # Se ejecutan las funciones
    usuario = escoge_usuario()
    usuario2 = escoge_usuario2()
    # Imprimimos las elecciones de los usuarios
    print(f"\nUsuario 1 eligió: {usuario}")
    print(f"Usuario 2 eligió: {usuario2}")
    # Se ejecutan la función
    resultado = ganador(usuario, usuario2)
    # Imprimimos resultado
    print(f"\nUsuario 1 {resultado}")

# Iniciamos el juego
jugar()
