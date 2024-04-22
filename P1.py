# Función para calcular el nivel de rendimiento y el dinero recibido
def calcular_rendimiento(salario, puntuacion):
    # Definir los niveles de rendimiento y los rangos de puntuación correspondientes
    niveles_de_rendimiento = {
        "Inaceptable": (0, 3),
        "Aceptable": (4, 6),
        "Meritorio": (7, 10)
    }
    
    # Calcular el dinero recibido en base a la puntuación
    dinero_recibido = salario * (puntuacion / 10)
    
    # Determinar el nivel de rendimiento en base a la puntuación
    nivel_de_rendimiento = None
    for nivel, (limite_inferior, limite_superior) in niveles_de_rendimiento.items():
        if limite_inferior <= puntuacion <= limite_superior:
            nivel_de_rendimiento = nivel
            break
    
    return nivel_de_rendimiento, dinero_recibido

# Entrada: salario y puntuación
salario = float(input("Ingresa tu salario mensual: "))
puntuacion = int(input("Ingresa tu puntuación de rendimiento (0-10): "))

# Calcular el nivel de rendimiento y el dinero recibido
rendimiento, dinero = calcular_rendimiento(salario, puntuacion)

# Imprimir el resultado
print(f"Nivel de Rendimiento: {rendimiento}")
print(f"Cantidad de Dinero Recibido: ${dinero:.2f}")
