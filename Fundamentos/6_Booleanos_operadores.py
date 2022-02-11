# Booleanos
# Dos tipos 
# Truen & False

# True -> 1
# False -> 0


variable1 = True
variable2 = False

print(type(variable1))
print(variable1.bit_length())

## Operadores
# Asignación (=)
# Operadores matemáticos
# String (+) concatenación

# Asignación complementarios 
x = 4
x += 5
print(x)
x **= 2
print(x)

# Conjunción -> and
print(variable1 and variable2)
print(True and True)
print(False and False)

# Disyunción -> or 
print('OR')
print(variable1 or variable2)
print(False or False)

# Negación
print(not variable1)
print(not variable2)

# Operadores bit a bit % | ^
print('1: ',True ^ True) # Entrega False porque convierte a binario y después hace la operacion
print('2: ',True and True) # Entrega True porque hace la operacion lógica de toda la expresión

# Conversión
print(4 ^ 5) 
print(4 | 5) 

print('3: ',True & True) # Entrega False


# Desplazamiento bit a bit hacia la derecha
print(True >> False)

# Desplazamiento bit a bit hacia la izquierda
print(True << False)

# Operadores Bit 
var1 = 2 # 1 0
var2 = 3 # 1 1
var3 = 5 # 1 0 1 

print('Probando los binarios')
print(var1 & var2)
print(var1 | var2)
print(var1 ^ var2)

