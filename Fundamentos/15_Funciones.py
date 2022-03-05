# Funciones ->def
# A regla de correspondencia -> B
# a -> f ->b

# Cuando no hay un retorno en un def no se lo puede llamar como funcion si no como un procedimiento

def procedimiento():
    print('Hola mundo')

procedimiento()

edades = [18,5,20,22,17,14,5,2]

# Funciones 
def esMayorEdad(edad: int):
    if edad >=18:
        return True
    return False

for edad in edades:
    print(esMayorEdad(edad))

# Recibir varios parametros
def saludar2(nombre: str, apellido:str):
    return (f'Saludos {nombre} {apellido}')

print(saludar2('Janeth','Castillo'))

# Parametros por defecto 
def saludar3(nombre = 'Victor',apellido = 'Jara'):
    return (f'Saludos {nombre} {apellido}')
print(saludar3())
print(saludar3('Sara'))
print(saludar3('Alberto','Gaibor'))


# LLamar una función dentro de una función 
def saludar4():
    print('Hola mundo')
    print(saludar3())

saludar4()

# Documentacion
def calcularCubo(numero: int):
    '''
    Permite calcular el cubo de un número 
    numero: Número entero 
    return: El cubo de la entrada
    '''
    return numero**3

print(calcularCubo(3))
print(calcularCubo.__doc__)

# Funciones args
# *args
# Número indefinido de valores
def listarAlumnos(*alumnos):
    print(f'Alumno: {alumnos}')

listarAlumnos('Anderson')
listarAlumnos('Anderson','Viv','Samy','Juan')

def listarAlumnos2(*alumnos):
    for alumno in alumnos:
        print(f'Alumno: {alumno}')

listarAlumnos2('Anderson')
listarAlumnos2('Anderson','Viv','Samy','Juan')


# **kargs
# Número indefinido de parámetros
def listarAlumnos3(**alumnos):
    print(f'La edad es: {alumnos[edad]}')

listarAlumnos3(nombre = 'Jane', apellido = 'Castillo', edad = 29)