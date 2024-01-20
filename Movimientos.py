
import Validaciones as val

def obtener_coordenadas() -> tuple:
    """Obtiene las coordenadas (fila, columna) del usuario.

    pre:

    post:Devuelve un tuple con dos enteros representando las coordenadas (fila, columna)
    ingresadas por el usuario.
    """
    while True:
        try:
            fila = int(input('Fila objetivo: '))
            columna = int(input('Columna objetivo: '))
            return fila, columna
        except ValueError:
            print('Ingrese coordenadas válidas (números enteros).')
            

def mov_peon_b(a, b, tablero) -> None:
    """Mueve el peón blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual del peón blanco en el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas en diagonal si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        if tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif val.validar_peon(a, b, fin_f, fin_c, tablero, 'b'):
            print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            contador += 1
            continue


def mov_peon_n(a, b, tablero) -> None:
    """Mueve el peón negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual del peón negro en el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas en diagonal si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif val.validar_peon(a, b, fin_f, fin_c, tablero, 'n'):
            print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            contador += 1
            continue



def mov_torre_b(a, b, tablero) -> None:
    """Mueve la torre blanca desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual de la torre blanca en
    el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
        
        # Verifica si el movimiento es válido
        if (fin_c != b) and (fin_f != a):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'reyb') and (tablero[a][b] == 'torreb') and enroque_blanco and valido:
            print('¡Enroque!')
            enroque_blanco = False
            if fin_c < b:
                tablero[fin_f][fin_c] = tablero[fin_f][fin_c + 2]
                tablero[a][b] = tablero[fin_f][fin_c + 1]
            else:
                tablero[fin_f][fin_c] = tablero[fin_f][fin_c - 2]
                tablero[a][b] = tablero[fin_f][fin_c - 1]
            break
                contador += 1
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            # Elimina la pieza enemiga
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break
        elif valido:
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break
        else:
            print('Movimiento inválido')
            contador += 1

            
def mov_torre_n(a, b, tablero) -> None:
    """Mueve la torre negra desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual de la torre negra en
    el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
        
        # Verifica si el movimiento es válido
        if (fin_c != b) and (fin_f != a):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'reyn') and (tablero[a][b] == 'torren') and enroque_blanco and valido:
            print('¡Enroque!')
            enroque_blanco = False
            if fin_c < b:
                tablero[fin_f][fin_c] = tablero[fin_f][fin_c + 2]
                tablero[a][b] = tablero[fin_f][fin_c + 1]
            else:
                tablero[fin_f][fin_c] = tablero[fin_f][fin_c - 2]
                tablero[a][b] = tablero[fin_f][fin_c - 1]
            break
                contador += 1
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            # Elimina la pieza enemiga
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break
        elif valido:
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break
        else:
            print('Movimiento inválido')
            contador += 1

            
            
            
def mov_alfil_b(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_alfil(a, b, fin_f, fin_c, tablero)
        
        if (fin_c == b) or (fin_f == a) or ((a - fin_f) != (b - fin_c)):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif ('' in tablero[fin_f][fin_c]) and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Casilla ocupada. Inténtelo de nuevo.")
            contador += 1


def mov_alfil_n(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_alfil(a, b, fin_f, fin_c, tablero)
        
        if (fin_c == b) or (fin_f == a) or ((a - fin_f) != (b - fin_c)):
            print('Movimiento inválido.')
            contador += 1
            continue
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif ('' in tablero[fin_f][fin_c]) and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
        else:
            print("Casilla ocupada. Inténtelo de nuevo.")
            contador += 1
            

def mov_caballo_b(a, b, tablero) -> None:
    """Mueve el caballo blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:
    - a y b son enteros en el rango del tablero (0-7), representando la fila y columna de la posición
    actual del caballo blanco.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas si corresponde.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_caballo(a, b, fin_f, fin_c, tablero)
        
        if tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue
        
def mov_caballo_n(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_caballo(a, b, fin_f, fin_c, tablero)
        
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue

def mov_reina_b(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_reina(a, b, fin_f, fin_c, tablero)
        
        if tablero[fin_f][fin_c].endswith('b'):
                print('Movimiento inválido.')
                contador += 1
                continue
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")
            contador += 1
        
        
def mov_reina_n(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_reina(a, b, fin_f, fin_c, tablero)
        
        if tablero[fin_f][fin_c].endswith('n'):
                print('Movimiento inválido.')
                contador += 1
                continue
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")
            contador += 1


def mov_rey_b(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_rey(a, b, fin_f, fin_c)
        
        if tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            enroque_blanco = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            enroque_blanco = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue
        
def mov_rey_n(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_rey(a, b, fin_f, fin_c)
        
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            enroque_blanco = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            enroque_blanco = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue

def promocion(tablero, promos) -> None:
    if 'peonb' in tablero[0]:
        print('Peon blanco promociona')
        promocionado = promos[int(input('1-Torre, 2-Caballo, 3-Alfil, 4-Reina'))]
        tablero[0][tablero[0].index('peonb')] = promocionado + 'b'
    if 'peonn' in tablero[-1]:
        print('Peon negro promociona')
        promocionado = promos[int(input('1-Torre, 2-Caballo, 3-Alfil, 4-Reina'))]
        tablero[-1][tablero[-1].index('peonn')] = promocionado + 'n'

def movimiento_blanco(fila, columna, tablero) -> bool:
    if tablero[fila][columna] == 'peonb':
        mov_peon_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'torreb':
        mov_torre_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'alfilb':
        mov_alfil_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'caballob':
        mov_caballo_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reinab':
        mov_reina_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reyb':
        mov_rey_b(fila, columna, tablero)
        return False
    else:
        print('No hay una pieza blanca en esa posición')
        return True
    

def movimiento_negro(fila, columna, tablero) -> bool:
    if tablero[fila][columna] == 'peonn':
        mov_peon_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'torren':
        mov_torre_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'alfiln':
        mov_alfil_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'caballon':
        mov_caballo_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reinan':
        mov_reina_b(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reyn':
        mov_rey_b(fila, columna, tablero)
        return False
    else:
        print('No hay una pieza negra en esa posición')
        return True

enroque_blanco = True
enroque_negro = True
