# Conjuntos -> set

conjunto1 = {1,2,3,4}
print(conjunto1)
print(type(conjunto1))

conjunto2 = {1,2,3,4,4}
print(conjunto2)

# Crear una lista con elementos unicos 
listaEjemplo = [14,15,16,16,16,16,89,75,14,15]
conjunto3 = list(set(listaEjemplo))
print(conjunto3)

# Es posible crear conjuntos no numéricos
conjunto4 = {'Andrés','Bryan','Cristo','Andrés'}
print(conjunto4)


# Es posible crear conjuntos de diferentes tipos de datos 
conjunto5 = {78, True, False, 'Mily'}
print(conjunto5)

# Métodos de los conjuntos 
cA = {1,2,3,4,5,6,7}
cB = {3,4,5}

# Agregar un elemento al conjunto 
cA.add(8)
print(cA)

cA.add(1)
print(cA)

# Tamaño del conjunto
print(len(cA))

# Eliminar un elemento del conjunto
cA.discard(8)
print(cA)

# Update del conjunto
cA.update({6,7,8,9})
print(cA)


# Copiar el conjunto 
cD = cA.copy()
print(cD)

# pop
cD.pop()
print(cD)

cD.clear()
print(cD)

# Método entre dos conjuntos
print('Conjunto A:', cA)
print('Conjunto B:', cB)

# Diferencia
print(cA.difference(cB))
# Unión
print(cA.union(cB))
# Intersección
print(cA.intersection(cB))
# Diferencia simétrica
print(cA.symmetric_difference(cB))

# Si dos conjuntos son disjuntos
print(cA.isdisjoint(cB))
cE = {200,300,400}
print(cA.isdisjoint(cE))

# Si es subconjunto
print(cB.issubset(cA))
# Si es superconjunto
print(cA.issubset(cB))