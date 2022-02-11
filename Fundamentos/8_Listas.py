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