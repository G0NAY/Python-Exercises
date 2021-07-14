##Basico para generar una matriz
matriz = []

filas = int(input("Numero de Filas: "))
columnas = int(input("Numero de Columnas: "))

for fila in range(filas):
    matriz.append([0]*columnas)

for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna] = int(input("Elemento %d,%d: " % (fila,columna)))

print(matriz)
