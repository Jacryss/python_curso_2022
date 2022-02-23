#n Diccionarios 
#Hash maps
# Tiene dos partes: clave (llave y el valor)
# Tras la inicializacion la clave es importante
# Clave puede ser cualquier tipo de datos
# No soporta la indexación

from sympy import per


diccionario1 = {
    'i1':1,
    'i2':5
}
print(type(diccionario1))
print(diccionario1)

print(diccionario1['i2'])

edad = 25
llaveVariable = 'cedula'

materias = {
    'estadística' : 8,
    'geometría' : 5
}

persona = {
    'nombre': 'Janeth',
    'apellido': 'Castillo',
    'edad' : 29,
    'casado' : False,
    29: True,
    llaveVariable : '17180017777',
    'materias' : materias,
    'universidad' :'UCE'

}




print(type(persona['nombre']))
print(type(persona['edad']))
print(persona['casado'])
print(persona[29])
print(persona['edad'])
print(persona['materias'])


# obtener un valor
print(persona.get('edad'))
# actualizar un dato
print(persona.update({'edad':23}))
print(persona)

#1. Conocer un valor del diccionario
print(persona.values())

#2. Conover únicamente la llave
print(persona.keys())

#3. Diccionario mapeado
print(persona.items())


def obtenerValor(valorBuscar):
    for llave,valor in persona.items():
        if valorBuscar==llave:
            return valor

def obtenerLlave(valorBuscar):
    for llave,valor in persona.items():
        if valorBuscar==valor:
            return llave

print('LLave Encontrada: ',obtenerLlave(23))
print('Valor Encontrado: ',obtenerValor('cedula'))

# Pop item elimina el último valor en el diccionario
print(persona)
persona.popitem()
print(persona)

# Que pasa si se pide un valor 
print(persona.get('universidad', 'No existe ese valor'))

copiaPersona = persona.copy()
print(copiaPersona)

# Numerable
print(len(copiaPersona))