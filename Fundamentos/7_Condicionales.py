# Si \, sino, entonces
# If, else, elif

variable1 = True
variable2 = False

# Operador de comparacion con dos iguales 
print(1==1)
if variable1 and variable2 == True:
    print('la expresion es vedadera')
else:
    print('la expresion es falsa')

texto ='Baneth'
# Python se puede omitir la comparación a verdadero,
# las dos siguientes expresiones son iguales
# if texto.startswith('J')== True:
if texto.startswith('J'):
    print('Tu nombre empieza con la letra J')
elif texto.startswith('B'):
    print('Tu nombre empieza con la letra B')
else:
    print('Tu nombre no empieza con la letra J ni con la letra B')