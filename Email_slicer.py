# Esta función toma un correo electrónico como argumento y verifica su dominio
def verificar_dominio(email):
    # Divide el correo electrónico en dos partes: nombre y dominio, usando '@' como separador.
    nombre, dominio = email.split('@')
    # Divide el nombre por un punto, toma la primera parte (suponiendo que es el primer nombre) y la capitaliza, se aplica al primer elemento de la lista  y convierte el primer caracter en mayúscula si no lo está 
    primer_nombre = nombre.split('.')[0].capitalize()
    
    # Creamos un diccionario de dominios de emails populares y la empresa, clave-valor
    dominios_populares = {'gmail.com': 'Google', 'yahoo.com': 'Yahoo', 'outlook.com': 'Microsoft Outlook'}
    
    # Verificar si el dominio es personalizado o popular
    if dominio in dominios_populares:
        return f"Hey {primer_nombre}, veo que tu correo electrónico está registrado en {dominios_populares[dominio]}. ¡Genial!"
    else:
        # Aplica metodo que en primer_nombre
        dominio_personalizado = dominio.split('.')[0].capitalize()
        return f"Hey {primer_nombre}, veo que tienes tu propia configuración en {dominio_personalizado}. ¡Impresionante!"

# Solicitar al usuario su email
email_usuario = input("Ingresa tu dirección de correo electrónico: ")
# Imprimimos el resultado de la función con el email proporcionado como argumento
print(verificar_dominio(email_usuario))
