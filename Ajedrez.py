
import Movimientos as mov

def imprimir_tablero(tablero) -> None:
    """Imprime el tablero de ajedrez con las piezas actuales.

    pre:
    - tablero es una matriz que representa el estado actual del tablero de ajedrez.
      Cada elemento de la lista interior es una cadena de texto que representa una pieza en la
      posición correspondiente.

    post:
    - Imprime el tablero de ajedrez con las filas numeradas y las columnas etiquetadas.
    - Cada casilla tiene un ancho fijo.
    - Las filas están numeradas en el lado izquierdo del tablero.
    - Las columnas están etiquetadas en la parte superior del tablero.
    - Se utilizan bordes para delimitar las casillas y dar estructura visual al tablero.
    """
    ancho_casilla = 9
    ancho_tablero = (ancho_casilla + 1) * len(tablero[0]) + 1
    
    # Imprime las etiquetas de las columnas
    print("      0           1            2           3           4          5            6          7")
    print(" +" + "-----------+" * len(tablero[0])) 

    for i, fila in enumerate(tablero, 0):
        print(f"{i}|", end=" ") # Imprime el número de fila y los bordes
        
        '''Imprime cada casilla del tablero con formato ordenado y alineado, utilizando ancho fijo
        y separando con "|".'''
        print(" | ".join([f"{casilla:<{ancho_casilla}}" for casilla in fila]), end=" |")
        
        print("\n +" + "-----------+" * len(tablero[0])) # Imprime los bordes inferiores de las casillas

tablero = [['torren', 'caballon', 'alfiln', 'reinan', 'reyn', 'alfiln', 'caballon', 'torren'],
           ['peonn', 'peonn', 'peonn', 'peonn', 'peonn', 'peonn', 'peonn', 'peonn'],
           ['' for _ in range(8)],
           ['' for _ in range(8)],
           ['' for _ in range(8)],
           ['' for _ in range(8)],
           ['peonb', 'peonb', 'peonb', 'peonb', 'peonb', 'peonb', 'peonb', 'peonb'],
           ['torreb', 'caballob', 'alfilb', 'reinab', 'reyb', 'alfilb', 'caballob', 'torreb']]

promos = ('torre', 'caballo', 'alfil', 'reina')

mov_b = True
mov_n = False


while True:
    imprimir_tablero(tablero)
    while mov_b:
        try:
            jugada_i_f = int(input('Fila de pieza blanca a mover: '))
            jugada_i_c = int(input('Columna de pieza blanca a mover: '))
            if jugada_i_f == 69:
                print('El jugador blanco se rinde')
                break
            if mov.movimiento_blanco(jugada_i_f, jugada_i_c, tablero):
                continue
            mov_b, mov_n = False, True
        except ValueError:
            print('Ingrese las coordenadas en entero.')
    mov.promocion(tablero, promos)
    imprimir_tablero(tablero)
    if 'reyn' not in tablero:
        print('El jugador blanco gana')
        break
    while mov_n:
        try:
            jugada_i_f = int(input('Fila de pieza negra a mover: '))
            jugada_i_c = int(input('Columna de pieza negra a mover: '))
            if jugada_i_f == 69:
                print('El jugador negro se rinde')
                break
            if mov.movimiento_negro(jugada_i_f, jugada_i_c, tablero):
                continue
            mov_b, mov_n = True, False
        except ValueError:
            print('Ingrese las coordenadas en entero.')
    mov.promocion(tablero, promos)
    imprimir_tablero(tablero)
    if 'reyb' not in tablero:
        print('El jugador negro gana')
        break
