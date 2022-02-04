# Programa que permite resolver ecuaciones de segundo grado
# ax^(2)+bx+c = 0 //a,b y c son números enteros

# Usuario ingrese por consola valores de: a, b y c 
# Imprimiremos por consola separado por comas
# Mostrar las dos soluciones x1 y x2
import math

a = int(input('Ingrese a: '))
b = int(input('Ingrese b: '))
c = int(input('Ingrese c: '))


x1 = (-b+math.sqrt((b**2)-(4*a*c)) )/(2*a)
x2 = (-b-math.sqrt((b**2)-(4*a*c)) )/(2*a)
print(x1)
print(x2)