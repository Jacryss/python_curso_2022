# Manejo de los archivos
# Windows texto y binario

miarchivo = open('Scripting/Archivos/ejemplo.txt', 'r',)
print(miarchivo)
print(type(miarchivo))

print(miarchivo.read())
print('----------------')

miarchivo.seek(0)
print(miarchivo.read())

# Leer  varias lineas
print('Read varias lineas')

miarchivo.seek(0)
print(miarchivo.readlines())