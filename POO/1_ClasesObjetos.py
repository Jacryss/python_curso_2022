# POO
# Atributo, plantilla

# Clase
# Atributos (características y metodos)

class Curso: 
    #Atributos
    # Metodos
    pass


class Alumno:
    pass
# Instaciar una clase -> objeto

curso1 = Curso()
curso2 = Curso()

print(type(curso1))

cursos = [curso1, curso2]
print(cursos)

print('Comprobar si curso1 es instancia de Curso', isinstance(curso1, Curso))
print('Comprobar si curso1 es instancia de Curso', isinstance(curso1, Alumno))
