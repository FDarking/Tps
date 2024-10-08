"""
Las siguientes matrices responden distintos patrones de relleno. Desarrollar funciones que 
generen cada una de ellas sin intervención humana y escribir un programa
que las invoque e imprima por pantalla. El tamaño de las matrices debe establecerse como N x N, 
donde N se ingresa a través del teclado.

a:  1 0 0 0              b: 0 0 0 27          c: 4 0 0 0
    0 3 0 0                 0 0 9 0              3 3 0 0
    0 0 5 0                 0 3 0 0              2 2 2 0
    0 0 0 7                 1 0 0 0              1 1 1 1

d:  8 8 8 8              e: 0 1 0 2           f: 0 0 0 1
    4 4 4 4                 3 0 4 0              0 0 3 2
    2 2 2 2                 0 5 0 6              0 6 5 4
    1 1 1 1                 7 0 8 0             10 9 8 7

g:  1 2 3 4              h: 1 2 4 7           i: 1 2 6 7
   12 13 14 5              3 5 8 11             3 5 8 13
   11 16 15 6              6 9 12 14            4 9 12 14
    10 9 8 7               10 13 15 16         10 11 15 16
"""
num = int(input("Ingrese el tamaño de la matriz (N x N): "))

def a_matriz(n: int) -> list[list[int]]:
    # Crea una matriz cuadrada en donde la primera diagonal incrementa de forma consecutiva
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i] = i * 2 + 1
    return matriz

def b_matriz(n: int) -> list[list[int]]:
    # Crea una matriz cuadrada en donde la diagonal paralela incrementa de forma consecutiva
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][n - i - 1] = 3 ** (n - i - 1)
    return matriz

def c_matriz(n: int) -> list[list[int]]:
    # Crea una matriz donde los valores son el mínimo entre fila y columna
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                matriz[i][j] = min(i + 1, j + 1)
    return matriz

def d_matriz(n: int) -> list[list[int]]:
    # Crea una matriz donde cada fila tiene el mismo valor
    matriz = [[n - i for _ in range(n)] for i in range(n)]
    return matriz

def e_matriz(n: int) -> list[list[int]]:
    # Crea una matriz alternando números de fila y columna
    matriz = [[i + 1 if j % 2 == 0 else j + 1 for j in range(n)] for i in range(n)]
    return matriz

def f_matriz(n: int) -> list[list[int]]:
    # Crea una matriz con un patrón descendente
    matriz = [[(n - i - 1) * n + (n - j - 1) for j in range(n)] for i in range(n)]
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(f"{fila}")

print("Matriz A:")
for fila in a_matriz(num):
    print(f"{fila}")

print("\nMatriz B:")
for fila in b_matriz(num):
    print(f"{fila}")

print("\nMatriz C:")
imprimir_matriz(c_matriz(num))

print("\nMatriz D:")
imprimir_matriz(d_matriz(num))

print("\nMatriz E:")
imprimir_matriz(e_matriz(num))

print("\nMatriz F:")
imprimir_matriz(f_matriz(num))
