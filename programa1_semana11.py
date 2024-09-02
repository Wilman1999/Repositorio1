import random


def generate_random_matrix(rows, cols, min_val, max_val):
    """
    Genera una matriz con valores aleatorios dentro de un rango específico.

    :param rows: Número de filas en la matriz
    :param cols: Número de columnas en la matriz
    :param min_val: Valor mínimo que puede contener la matriz
    :param max_val: Valor máximo que puede contener la matriz
    :return: Matriz generada con valores aleatorios
    """
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def search_in_matrix(matrix, target):
    """
    Busca un valor en la matriz y devuelve su posición si se encuentra.

    :param matrix: Lista de listas representando la matriz 2D
    :param target: Valor a buscar
    :return: Tupla que contiene la posición (fila, columna) o None si no se encuentra
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return (i, j)
    return None


def get_valid_value():
    """
    Solicita al usuario un valor entre 1 y 9 y asegura que sea válido.

    :return: Un valor entero entre 1 y 9
    """
    while True:
        try:
            value = int(input("Introduce el valor a buscar (entre 1 y 9): "))
            if 1 <= value <= 9:
                return value
            else:
                print("Por favor, ingresa un número entre 1 y 9.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")


def print_matrix(matrix):
    """
    Imprime la matriz de manera formateada.

    :param matrix: Lista de listas representando la matriz 2D
    """
    print("Matriz actual:")
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    # Definir el tamaño de la matriz y el rango de valores
    rows, cols = 3, 3
    min_val, max_val = 1, 9

    # Generar una matriz aleatoria
    matrix = generate_random_matrix(rows, cols, min_val, max_val)

    # Solicitar al usuario el valor a buscar
    target_value = get_valid_value()

    # Buscar el valor en la matriz
    position = search_in_matrix(matrix, target_value)

    # Mostrar la matriz
    print_matrix(matrix)

    # Mostrar el resultado de la búsqueda
    if position:
        print(f"El valor {target_value} se encontró en la posición: {position}")
    else:
        print(f"El valor {target_value} no se encontró en la matriz.")


if __name__ == "__main__":
    main()
