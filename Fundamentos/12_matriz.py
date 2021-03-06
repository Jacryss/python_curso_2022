# Para crear una matriz
def crearMatriz():
    matriz = []
    nFilas = int(input('Ingrese el número de filas: '))
    nColumnas = int(input('Ingrese el número de columnas: '))
    for i in range(nFilas):
        matriz.append([0]*nColumnas)
    for i in range(0, nFilas):
        for j in range (0, nColumnas):
            mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            matriz[i][j] = int(input(mensaje))
    dimensiones = (nFilas,nColumnas)
    return matriz, dimensiones

# Para imprimir cualquier matriz
def mostrarMatriz(matriz,dimensiones):
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end = '\t')
        print('')
    pass

def main():
    matriz, dimensiones = crearMatriz()
    print(matriz)
    mostrarMatriz(matriz, dimensiones)
main()