# Importar librerías necesarias (en este caso no se requiere, pero puede ser útil en el futuro)
import os


# Función para crear y escribir notas en un archivo
def escribir_notas(nombre_archivo, notas):
    """Crea un archivo y escribe notas en él."""
    try:
        with open(nombre_archivo, 'w') as file:
            for nota in notas:
                file.write(nota + '\n')  # Escribir cada nota en una nueva línea
        print(f"Notas escritas exitosamente en {nombre_archivo}.")
    except Exception as e:
        print(f"Ocurrió un error al escribir en el archivo: {e}")


# Función para leer notas de un archivo
def leer_notas(nombre_archivo):
    """Lee y muestra las notas desde un archivo."""
    try:
        with open(nombre_archivo, 'r') as file:
            print("\nContenido de las notas:")
            for line in file:
                print(line.strip())  # Imprimir cada línea sin saltos de línea
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


# Función principal para ejecutar el programa
def main():
    nombre_archivo = 'my_notes.txt'

    # Notas a escribir en el archivo
    notas = [
        "Esta es la primera línea de mis notas.",
        "Aquí está la segunda línea de mis pensamientos.",
        "Y esta es la tercera línea de notas importantes.",
        "No olvides revisar la lista de tareas pendientes.",
        "Recuerda beber suficiente agua a lo largo del día."
    ]

    # Escribir notas en el archivo
    escribir_notas(nombre_archivo, notas)

    # Leer y mostrar las notas del archivo
    leer_notas(nombre_archivo)


# Comprobar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()
