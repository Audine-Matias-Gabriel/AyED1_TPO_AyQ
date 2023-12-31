
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
        
        if val.validar_peon(a, b, fin_f, fin_c, tablero, 'b'):
            # para capturar en diagonal
            if tablero[fin_f][fin_c].endswith('n'):
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('b'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_peon(a, b, fin_f, fin_c, tablero, 'n'):
            # para capturar en diagonal
            if tablero[fin_f][fin_c].endswith('b'):
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('n'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        # Verifica si el movimiento es válido
        if (fin_c != b) and (fin_f != a):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'reyb') and (tablero[a][b] == 'torreb') and enroque_blanco:
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                print('¡Enroque!')
                enroque_blanco = False
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
                contador += 1
        elif tablero[fin_f][fin_c] != '':
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                # Elimina la pieza enemiga
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
                
                # Mueve la torre
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
                contador += 1
        else:
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break

            
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
        
        if (fin_c != b) and (fin_f != a):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'reyn') and (tablero[a][b] == 'torren') and enroque_negro:
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                print('¡Enroque!')
                enroque_negro = False
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
                contador += 1
        elif tablero[fin_f][fin_c] != '':
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                # Elimina la pieza enemiga
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
                
                # Mueve la torre
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
                contador += 1
        else:
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break

            
            
            
def mov_alfil_b(a, b, tablero) -> None:
    contador = 0
    while True:
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        if (fin_c == b) or (fin_f == a) or ((a - fin_f) != (b - fin_c)):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif ('' in tablero[fin_f][fin_c]):
            # Valida movimiento y captura
            if val.validar_alfil(a, b, fin_f, fin_c, tablero):
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                return
            else:
                print("Movimiento inválido.")
                contador += 1
        # Captura diagonal
        elif tablero[fin_f][fin_c].endswith('n'):
            if val.validar_alfil(a, b, fin_f, fin_c, tablero):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                return
            else:
                print("Movimiento inválido.")
                contador += 1
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
        
        if (fin_c == b) or (fin_f == a) or ((a - fin_f) != (b - fin_c)):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif ('' in tablero[fin_f][fin_c]):
            valido = val.validar_alfil(a, b, fin_f, fin_c, tablero)
            if valido:
                if tablero[fin_f][fin_c].endswith('b'):
                    print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                    tablero[fin_f][fin_c] = ''
                elif tablero[fin_f][fin_c].endswith('n'):
                    print('Movimiento inválido.')
                    contador += 1
                    continue
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                return
            else:
                print("Movimiento inválido.")
                contador += 1
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
        
        if val.validar_caballo(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c].endswith('n'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('b'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_caballo(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c].endswith('b'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('n'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_reina(a, b, fin_f, fin_c, tablero):
            # Captura diagonal
            if tablero[fin_f][fin_c].endswith('n'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('b'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_reina(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c].endswith('b'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('n'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_rey(a, b, fin_f, fin_c):
            # Capturar pieza enemiga si la hay
            if tablero[fin_f][fin_c].endswith('n'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('b'):
                print('Movimiento inválido.')
                contador += 1
                continue
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
        
        if val.validar_rey(a, b, fin_f, fin_c):
            # Capturar pieza enemiga si la hay
            if tablero[fin_f][fin_c].endswith('b'):
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
                tablero[fin_f][fin_c] = ''
            elif tablero[fin_f][fin_c].endswith('n'):
                print('Movimiento inválido.')
                contador += 1
                continue
            enroque_negro = False
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
    if 'peonb' in tablero[0]:
        print('Peon negro promociona')
        promocionado = promos[int(input('1-Torre, 2-Caballo, 3-Alfil, 4-Reina'))]
        tablero[0][tablero[0].index('peonn')] = promocionado + 'n'

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
        return True
    

def movimiento_negro(fila, columna, tablero) -> bool:
    if 'peonn' in tablero[fila][columna]:
        mov_peon_n(fila, columna, tablero)
        return False
    elif 'torren' in tablero[fila][columna]:
        mov_torre_n(fila, columna, tablero)
        return False
    elif 'alfiln' in tablero[fila][columna]:
        mov_alfil_n(fila, columna, tablero)
        return False
    elif 'caballon' in tablero[fila][columna]:
        mov_caballo_n(fila, columna, tablero)
        return False
    elif 'reinan' in tablero[fila][columna]:
        mov_reina_n(fila, columna, tablero)
        return False
    elif 'reyn' in tablero[fila][columna]:
        mov_rey_n(fila, columna, tablero)
        return False
    else:
        return True

enroque_blanco = True
enroque_negro = True
