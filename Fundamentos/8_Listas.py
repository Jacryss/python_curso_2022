# Listas list()
# Inicialoización[]

lista1 = [1,2,3,4,5,6,7,8,9,10]
print(type(lista1))

lista2 = ['a','b','c',80,20, True, False]
print(lista2)

# Métodos y las operaciones e listas
# Indexación 
# Número de elementos lista
print(len(lista1))
print(lista2[0])

lista2[5] = False
print(lista2[1:3])
print(lista2[::-1])

listaAlumnos = ['Anderso','Andres','Cristo','Janeth','Mario']
listaAlumnos2 =listaAlumnos[1:]
print(listaAlumnos2)
print(type(listaAlumnos2))

# Agregar datos a una lista (final)
listaAlumnos2.append('Fernanda')
print(listaAlumnos2)

# Agregar datos en una posición específica
listaAlumnos2.insert(3,'Bryan')
print(listaAlumnos2)

# Como agregar al final otra lista
listaAlumnos2.extend(['Pablo','José'])
print(listaAlumnos2)


# Retirar elementos de la lista (pop)
# pop recibe el índice que quiero eliminar, si no se le indica retira el último elemento 
listaAlumnos2.pop()
print(listaAlumnos2)

# Retirar elemento especifico
listaAlumnos2.pop(1)
print(listaAlumnos2)

# Retirar elemento especifico por el nombre
listaAlumnos2.remove('Pablo')
print(listaAlumnos2)

# ¿Qué pasa si existen dos elementos iguales? Se retira uno 
listaAlumnos2.extend(['Alejandro','Alejandro'])
print(listaAlumnos2)

listaAlumnos2.remove('Alejandro')
print(listaAlumnos2)

# Operador 
print('Andres' in listaAlumnos2)
print('Sammy' in listaAlumnos2)

# Hacer una copia
CopiaListaAlumnos =listaAlumnos2[::]
print(CopiaListaAlumnos)
CopiaListaAlumnos2 = CopiaListaAlumnos.copy()
print(CopiaListaAlumnos2)

# Invertir la copia
print(CopiaListaAlumnos[::-1])
CopiaListaAlumnos2.reverse()
print(CopiaListaAlumnos2)

# Encontrar índice de una lista
print(CopiaListaAlumnos.index('Janeth'))

# ¿Qué pasaría si solicito un índice de un elemento que no se encuentra en la list?
# print(CopiaListaAlumnos.index(58))

# Ordenar 
CopiaListaAlumnos.sort()
print(CopiaListaAlumnos)


lista4 = [10,60,19,19,45]
lista4.sort()
print(lista4)

# Ordenar una lista con diferentes tipos de datos no es posible
# lista5 = ['a',10,60,19,19,45]
# lista5.sort()
# print(lista5)

# Pueden convertir un string a una lista
cadenaTexto = 'Las Universidad piensan retornar a la presencialidad'
listadeTexto = list(cadenaTexto)
print(listadeTexto)

# Separar en palabras
listaPalabra = cadenaTexto.split(' ')
print(listaPalabra)

# Contar el número de veces que una palabra está en la lista
print(listaPalabra.count('Universidad'))

# Join 
saludo = 'Saludo: '
oracion = saludo.join([])