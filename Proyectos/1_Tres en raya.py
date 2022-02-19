# Tres en raya
# Reglas clásica del tres en línea
# Si tres caracteres son iguales en cualquier sentido se termina e juego
# Vana  existir dos jugadores
# Presentación
# Se pueden asignar nombres a los dos jugadores
# Matriz creada a partir de listas
# Se solicitará que se ingrese la fila y la columna en la que el jugador quiere marcar su movimiento
# Deberá comprobar si se encuentra ocupado perderá el turno
# Se terminará el juego 
# Se presente un menú al inicio en el que se pueda ingresar los nombre 
# de los jugadores, y adempas escoger los caracteres, por defeco sera la x ye l o
# Y la tercera opción será jugar
# Y la cuarta salir

global nombreJugador1
nombreJugador1 = 'Jugador1'
global nombreJugador2
nombreJugador2 = 'Jugador2'

global piezaJugador1
piezaJugador1 = 'X'
global piezaJugador2
piezaJugador3 = '0'

def menu():
    print('\n\tTres en raya\n')
    print('1. Nombres jugadores')
    print('2. Cambiar piezas')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opción: ')
    # print('Desde adentro de la opicón menú', opcion)
    return opcion

def nombreJugadores():
    print('\n\tNombre jugadores')
    print('1. Cambiar nombre jugador 1')
    print('2. Cambiar nombre jugador 2')
    opcionNombre = input('Cambiar nombre del jugador:')

    if opcionNombre == '1':
        global nombreJugador1
        nombreJugador1 = input('Nombre jugador 1: ')

    elif opcionNombre == '2':
        global nombreJugador2
        nombreJugador2 = input('Nombre jugador 2: ')
    else:
        print('Por favor ingrese una opción válida')

def cambiarPiezas():
    print('\n\tPiezas')    
    print('1. Cambiar pieza del jugador 1')
    print('2. Cambiar pieza del jugador 2')
    opcionPieza = input('Cambiar pieza del jugador: ')    
    global piezaJugador1
    global piezaJugador2
    if opcionPieza == '1':
        print('Opcion 1')
        auxPieza1 = input('Pieza del jugador 1: ')       
        if  auxPieza1 != piezaJugador2:
            global piezaJugador1   
            piezaJugador1 = auxPieza1
        else:
            print('La pieza ingresada es igual a la del otro jugador')

    elif opcionPieza == '2':
        auxPieza2 = input('Pieza del jugador 2: ')  
        if auxPieza2 != piezaJugador1:            
            piezaJugador2 = auxPieza2
        else:
            print('La pieza ingresada es igual a la del otro jugador')

    else:
        print('Ingrese una opción válida')



def jugar():
    print('Jugando....')
    print('Es turno del jugador1',nombreJugador1)   

def mostrarTablero():
    pass

def main():
    opcionMenu = menu() # ejecuta la opción menú y también va asignar el retorno de mi variable 
    # Condicionales 
    if opcionMenu == '1':
        nombreJugadores()
    elif opcionMenu == '2':
        print('Cambia las piezas')
    elif opcionMenu == '3':
        jugar()
    elif opcionMenu == '4':
        print('Saliento...')         
    else:
        print('Por favor ingrese una opción válida')

    jugar()

    
main()

