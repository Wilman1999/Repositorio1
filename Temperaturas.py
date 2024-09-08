# Matriz 3D para almacenar las temperaturas (en grados Celsius)
temperaturas = [
    [   # Ciudad 1: Quito
        [12, 14, 15, 16, 18, 17, 19],  # Semana 1
        [13, 14, 16, 18, 19, 17, 20],  # Semana 2
        [12, 13, 15, 16, 18, 17, 19],  # Semana 3
        [11, 13, 15, 17, 18, 16, 19]   # Semana 4
    ],
    [   # Ciudad 2: Guayaquil
        [29, 30, 30, 29, 28, 30, 29],  # Semana 1
        [30, 29, 29, 28, 29, 30, 30],  # Semana 2
        [29, 30, 30, 29, 28, 30, 29],  # Semana 3
        [30, 29, 29, 28, 30, 29, 30]   # Semana 4
    ],
    [   # Ciudad 3: Cuenca
        [14, 15, 16, 17, 16, 15, 14],  # Semana 1
        [13, 14, 16, 17, 15, 14, 13],  # Semana 2
        [12, 13, 15, 16, 14, 13, 12],  # Semana 3
        [11, 12, 14, 15, 13, 12, 11]   # Semana 4
    ]
]

ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Calcular el promedio de temperaturas para cada ciudad por semana
for i, ciudad in enumerate(temperaturas):
    print(f"Temperaturas promedio por semana en {ciudades[i]}:")
    for semana_num, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Semana {semana_num + 1}: {promedio:.2f}°C")
    print("\n")

# Imprimir matriz completa con encabezados de días
print("Matriz de temperaturas por día:")
print("        ", end="")
for dia in dias:
    print(f"{dia[:3]} ", end="")
print()

for i, ciudad in enumerate(temperaturas):
    print(f"{ciudades[i]:<10}", end=" ")
    for semana in ciudad:
        for temp in semana:
            print(f"{temp:>3} ", end="")
        print("\n          ", end="")
    print()
