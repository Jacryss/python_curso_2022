# String inmutable e indexeable 
x = 'Hola'
y = 'con todos'

# String de varias líneas
texto = '''En un lugar de la Mancha, de cuyo nombre no quiero acordarme, 
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca 
que carnero, salpicón las más noches, duelos y quebrantos los sábados
'''
print(texto)

texto2 = '''
primera  \t linea
segunda \n linea
tercera
'''

print(texto2)

# Operaciones
cadena1 = 'Python'
cadena2 = 'es un lenguaje de programacion'
numero1 = 8.5
print(type(numero1))

# Concatenación es unir dos variables de tipo string en una sola impresion

print(cadena1, '', cadena2)

print(cadena1, '-', cadena2, 'interpretado', numero1)

print(cadena1 + cadena2 + 'y además tengo este número' + str(numero1))

cadena3 = cadena1 + cadena2

print(cadena3)

################################# FORMATED STRINGS ############################
# String es inmutable no acepta que se modifique pero es indexable 

nombre = 'Janeth'
edad = 29
ira = 99
universidad = 'UOC'

#1. Basado en variables
print(f'1:Hola mi nombre es {nombre} y mi edad es {edad}')
# 2. Llama al método de la clase string
print('2:Hola mi nombre es {} y mi edad es {} y tengo un ira de {}'.format(nombre, edad, ira))
# 3. LLama al método format pero indicando la posicion
print('3:Hola mi nombre es {0} y mi edad es {1} y tengo un ira de {2}'.format(nombre, edad, ira))
# Con repetición 
print('Hola mi nombre es {0}, estudio en la {1} y además trabajo en {1}'.format(nombre, universidad))
# 4. Formated string con reasignación de variables 
print('Hola mi nombre es {VariableNombre}, estudio en la {VariableEdad} y tengo un ira de {VariableIra}'.format(VariableNombre= 'Janeth', VariableEdad = edad, VariableIra = ira))

################################# INDEXACIÓN #################################

cadenaTexto = 'Este es un curso de programación muy buen curso'
print(cadenaTexto[1])
print(cadenaTexto[2])
# Range
print(len(cadenaTexto))
print(cadenaTexto[0])
print(cadenaTexto[31])
print(cadenaTexto[-1])
print(cadenaTexto[-2])
print(cadenaTexto[-32])

print(cadenaTexto[0] + cadenaTexto[11] + cadenaTexto[8] + cadenaTexto[-5] + cadenaTexto[17] + cadenaTexto[22] + cadenaTexto[21])


letra = cadenaTexto[0]
print(letra)
letra = 'A'
print(letra)

# Indexacion en rangos
print(cadenaTexto[0:2])
print(cadenaTexto[0:10])
print(cadenaTexto[2:20])

print(cadenaTexto[2:20:3])

# Hasta el final 
print(cadenaTexto[2:])
print(cadenaTexto[:3])
print(cadenaTexto[:])
print(cadenaTexto[::])

# Ejercicion: Invierta toda la variable cadenaTexto
print(cadenaTexto[::-1])

# Funciones en python
print(cadenaTexto.upper())
print(cadenaTexto.lower())

print(cadenaTexto.capitalize())

# Encontrar en la cadena de texto
# en caso de encontrar se devuelve el índice
print(cadenaTexto.find('curso'))
print('Animales: tigre'.find('tigre'))
# Si no existe devuelve -1
print('Animales: tigre'.find('perro'))

# Validar si empieza con 
cadenaTexto2 = 'Los niños juegan en el parque'
print(cadenaTexto2.startswith('Los'))
print(cadenaTexto2.startswith('Las'))
print(cadenaTexto2.endswith('parque'))
print(cadenaTexto2.endswith('cine'))


#Reemplazar palabras
print(cadenaTexto2.replace('niños', 'niñas').replace('Los','Las'))