# Asignacion
#
from tkinter import Y


x = 5
print('el valor de la variable x es:' , x)

# Asignacion None quiere decir que la variable no tiene nada

variable1 = None
print(type(variable1))
print('El valor de la variable1 es', variable1)

# Inicializar una variable 
y = 10
print(y)

# Multiplicar por 2
y = y*2
print(y)

# Multiplicar por 2
print(y*2)
print(y)

# Asignacion con diferentes tipo
y = 'saludo'

# Multiples asignaciones
# Creas las variables a y b con los valores de 2 y 3
a = 2
b = 3

a, b, c, saludo = 2,3,5, 'Hola'
print(a+b+c)
print(saludo)

saludo2 = saludo
print(saludo2)

saludo = 'Buenas tardes'
print(saludo2)

# Ejercicio 
x1 = 4
y1 = x1+1
x1 = 2
print('X1 es igual a:',x1, 'y ' 'y1 es igual a:',y1)

x2, y2 = 10,11
z2 = x2
y2 = z2+2
print(x2, ' ', y2, ' ', z2)

x2,x2 = 1,5