# Función para calcular el promedio de temperaturas por ciudad
def calcular_promedio_temperaturas(temperaturas, ciudades):
    promedios_ciudades = {}

    # Iterar sobre cada ciudad
    for i, ciudad in enumerate(temperaturas):
        suma_temperaturas = 0
        total_dias = 0

        # Iterar sobre cada semana de la ciudad
        for semana in ciudad:
            suma_temperaturas += sum(semana)  # Sumar todas las temperaturas de la semana
            total_dias += len(semana)  # Contar los días (7 por semana)

        # Calcular el promedio para la ciudad
        promedio = suma_temperaturas / total_dias
        promedios_ciudades[ciudades[i]] = promedio  # Almacenar el promedio en un diccionario

    return promedios_ciudades


# Matriz 3D para almacenar las temperaturas (en grados Celsius)
temperaturas = [
    [  # Ciudad 1: Quito
        [12, 14, 15, 16, 18, 17, 19],  # Semana 1
        [13, 14, 16, 18, 19, 17, 20],  # Semana 2
        [12, 13, 15, 16, 18, 17, 19],  # Semana 3
        [11, 13, 15, 17, 18, 16, 19]  # Semana 4
    ],
    [  # Ciudad 2: Guayaquil
        [29, 30, 30, 29, 28, 30, 29],  # Semana 1
        [30, 29, 29, 28, 29, 30, 30],  # Semana 2
        [29, 30, 30, 29, 28, 30, 29],  # Semana 3
        [30, 29, 29, 28, 30, 29, 30]  # Semana 4
    ],
    [  # Ciudad 3: Cuenca
        [14, 15, 16, 17, 16, 15, 14],  # Semana 1
        [13, 14, 16, 17, 15, 14, 13],  # Semana 2
        [12, 13, 15, 16, 14, 13, 12],  # Semana 3
        [11, 12, 14, 15, 13, 12, 11]  # Semana 4
    ]
]

ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Llamar a la función para calcular los promedios
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

# Mostrar los promedios de cada ciudad
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")
