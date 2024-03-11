# Definimos una función que toma un argumento llamado palabra.
def palindromo(palabra):
    # Verificamos la palabra sea igual que en su versión inversa
    # [::-1] es una forma de slicing que se utiliza para invertir una cadena
    return palabra == palabra[::-1]

# Pedimos que ingrese cinco palabras separadas por espacios
# Usamos .split() para dividir la entrada en una lista de palabras.
palabras = input("Ingresa cinco palabras separadas por espacios: ").split()

# Creamos un diccionario vacío donde almacenaremos cada palabra
resultado = {}

# Iniciamos un bucle para iterar sobre cada palabra en la lista
for palabra in palabras:
    # Verificamos si palabra es un palíndromo y actualiza el diccionario con la respuesta adecuada para cada palabra 
    resultado[palabra] = "sí es palíndromo" if palindromo(palabra) else "no es palíndromo"

# Iniciamos otro bucle para iterar sobre los elementos del diccionario resultado.
for palabra, palindromo in resultado.items():
    # Imprimimos cada palabra y si es un palíndromo o no, según lo almacenado en el diccionario clave-valor
    print(f"{palabra}: {palindromo}")

