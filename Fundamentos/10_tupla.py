
tupla1 = (4,5,6,6)
print(tupla1)
print(type(tupla1))

print(tupla1[0])

# tupla1[0] = 8

tupla2 =(True,25, 'hola')
print(tupla2)

print(False in tupla2)
print('python' in tupla2)
print(25 in tupla2)
print(100 not in tupla2)

print(tupla1.index(5))

print('Tamaño de una tupla1', len(tupla1))
print('Cuantos números 6 están en la tupla1', tupla1.count(6))

# Descompresión de elementos 
dimensiones = (500,600)
dimensionX, dimensionY = dimensiones
print(dimensionX)
print(dimensionY)


# coNVERTIR UNA LISTA A UNA TUPLA 
lista1 = [85,26,98]