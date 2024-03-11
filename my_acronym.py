def hacer_acronimo(frase):
    # Dividimos la frase en palabras, tomamos la primera letra de cada palabra
    # .split() dividi una cadena de texto en una lista de palabras
    palabras = frase.split()
    # ''.join(...) une todos los caracteres obtenidos
    # palabras es una lista 
    # palabra[0] for palabra recorre cada palabra en la lista
    # .upper() convierte toda la cadena resultante a mayúsculas
    acronimo = ''.join(palabra[0] for palabra in palabras).upper()
    return acronimo

# Usuario ingresa la frase
frase_usuario = input("Ingrese el significado completo de una organización o concepto: ")
print("El acrónimo es:", hacer_acronimo(frase_usuario))
