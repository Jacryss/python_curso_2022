#Capicuas
# Palindromos
# Solicitar al usuario que ingrese por teclado un texto le vamos a indicar si lo ingresa es o no un palíndromo

# texto = input('Por favor ingrese una cadena de texto:')
texto = 'rececar'
print('Palabra de izquierda a derecha',texto)
print('Palabra de derecha a izquierda',texto[::-1])

if texto == texto[::-1]:
    print('La palabra es un palíndromo')
elif texto.lower() == texto[::-1]:
    print('La palabra es un palíndromo ignorando mayúsculas')
elif texto.replace('',' ') == texto[::-1].replace('',' '):
    print('La palabra es un palíndromo ignorando los espacios')
else:
    print('La palabra no es un palíndromo')

numero = int(input('ingresa un número:'))
if numero% 2 ==0:
    print('Es un número par')
else: 
    print('Es un número impar')

if numero>0:
    print('Es un número mayor que cero')
else: 
    print('Es un número menor que cero')

x = 4
x += 5
print(x)