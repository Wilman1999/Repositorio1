import random


def bubble_sort(arr):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo de Bubble Sort.

    :param arr: Lista de números a ordenar
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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


def print_matrix(matrix):
    """
    Imprime la matriz de manera formateada.

    :param matrix: Lista de listas representando la matriz 2D
    """
    print("Matriz:")
    for row in matrix:
        print(' '.join(map(str, row)))


def main():
    # Definir el tamaño de la matriz y el rango de valores
    rows, cols = 3, 3
    min_val, max_val = 1, 9

    # Generar una matriz aleatoria
    matrix = generate_random_matrix(rows, cols, min_val, max_val)

    # Mostrar la matriz original
    print("Matriz Original:")
    print_matrix(matrix)

    # Solicitar al usuario qué fila desea ordenar (1 a 3)
    while True:
        try:
            row_to_sort = int(input(f"Selecciona la fila a ordenar (1 a {rows}): ")) - 1
            if 0 <= row_to_sort < rows:
                break
            else:
                print(f"Por favor, selecciona un número entre 1 y {rows}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    # Mostrar la fila seleccionada
    print(f"\nFila seleccionada (fila {row_to_sort + 1}):")
    print(' '.join(map(str, matrix[row_to_sort])))

    # Ordenar la fila específica utilizando Bubble Sort
    bubble_sort(matrix[row_to_sort])

    # Mostrar la matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
