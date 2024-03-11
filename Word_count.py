# Preguntamo al usuario 
entrada_usuario = input("¿Qué tienes en mente hoy? ")

# Contamos la cantidad de palabras en la oración
#.split() separa las palabras utilizando espacios como separadores
#len(..) devuelve la cantidad de elementos que genera el metodo .split() 
cantidad_palabras = len(entrada_usuario.split())

# Mostramos el resultado
print(f"Oh bien, acabas de decirme lo que tienes en mente en {cantidad_palabras} palabras.")
