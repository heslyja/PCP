import datetime

nombre = input("¿Cómo te llamas? ")
#.isalpha() verifica si todos los caracteres en una cadena de texto son letras del alfabeto
while not nombre.isalpha():
    print("Incorrecta. Por favor, ingresa una respuesta válida")
    nombre = input("¿Cómo te llamas? ")

fecha_nacimiento = input("¿Cuál es tu fecha de nacimiento (dd/mm/aaaa): ")
while True:
    try:
    #datetime.datetime es la clase dentro del modulo
    #.strptime() parsea (analiza y convierte) una cadena de texto en un objeto datetime
    #%d/%m/%Y es el formato
    #.date() convierte el datetime en un date, es decir, sin la hora
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, '%d/%m/%Y').date()
    #datetime.date.today() es la fecha actual
        if fecha_nacimiento >= datetime.date.today():
            print("Incorrecta. Por favor, ingresa una respuesta válida")
        else:
            break
    except ValueError:
        print("Incorrecta. Por favor, ingresa una respuesta válida")

direccion = input("¿Cuál es tu dirección? ")
    #.isspace() verificar si todos los caracteres en una cadena de texto son espacios en blanco. 
    #not dirección verifica si la cadena esta vacia
    #si una de las dos se cumple, el bucle seguirá ejecutándose
while direccion.isspace() or not direccion:
    print("Incorrecta. Por favor, ingresa una respuesta válida")
    direccion = input("¿Cuál es tu dirección? ")
    
goles = input("¿Cuales son tus metas personales?")
    #.isalpha() verifica si todos los caracteres en una cadena de texto son letras del alfabeto
while not goles.isalpha():
    print("Incorrecta. Por favor, ingresa una respuesta válida")
    goles = input("¿Cuales son tus metas personales?")

print("\nMini biografía:")
print(f"Nombre: {nombre}")
print(f"Fecha de nacimiento: {fecha_nacimiento}")
print(f"Dirección: {direccion}")
print(f"Metas personales: {goles}")

