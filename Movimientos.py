
import Validaciones as val

def obtener_coordenadas():
    """Obtiene las coordenadas (fila, columna) del usuario.

    pre:

    post:Devuelve un tuple con dos enteros representando las coordenadas (fila, columna)
    ingresadas por el usuario.
    """
    while True:
        try:
            fila = int(input(f'Fila objetivo: '))
            columna = int(input(f'Columna objetivo: '))
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
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_peon(a, b, fin_f, fin_c, tablero, 'b'):
            # para capturar en diagonal
            if 'peon' in tablero[fin_f][fin_c] and tablero[fin_f][fin_c].endswith('n'):
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            continue


def mov_peon_n(a, b, tablero) -> None:
    """Mueve el peón negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual del peón negro en el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas en diagonal si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_peon(a, b, fin_f, fin_c, tablero, 'n'):
            # para capturar en diagonal
            if 'peon' in tablero[fin_f][fin_c] and tablero[fin_f][fin_c].endswith('b'):
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            continue



def mov_torre_b(a, b, tablero) -> None:
    """Mueve la torre blanca desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:a y b son enteros representando la fila y columna de la posición actual de la torre blanca en
    el tablero.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas si es posible.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        # Verifica si el movimiento es válido
        if (fin_c != b) and (fin_f != a):
            continue
        elif tablero[fin_f][fin_c] == 'reyb':
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                print(f'¡Enroque!')
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
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
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if (fin_c != b) and (fin_f != a):
            continue
        elif tablero[fin_f][fin_c] == 'reyn':
            valido = val.validar_torre(a, b, fin_f, fin_c, tablero)
            if valido:
                print(f'¡Enroque!')
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                break
            else:
                print('Movimiento no válido. Inténtelo de nuevo.')
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
        else:
            # Mueve la torre
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            break

            
            
            
def mov_alfil_b(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if (fin_c == b) or (fin_f == a):
            continue
        elif (a - fin_f) != (b - fin_c):
            continue
        elif ('' in tablero[fin_f][fin_c]):
            # Valida movimiento y captura
            valido = val.validar_alfil(a, b, fin_f, fin_c, tablero)
            if valido:
                # Captura diagonal
                if tablero[fin_f][fin_c] != '':
                    print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                return
            else:
                print("Movimiento inválido.")
        else:
            print("Casilla ocupada. Inténtelo de nuevo.")


def mov_alfil_n(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if (fin_c == b) or (fin_f == a):
            continue
        elif (a - fin_f) != (b - fin_c):
            continue
        elif ('' in tablero[fin_f][fin_c]):
            valido = val.validar_alfil(a, b, fin_f, fin_c, tablero)
            if valido:
                if tablero[fin_f][fin_c] != '':
                    print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
                return
            else:
                print("Movimiento inválido.")
        else:
            print("Casilla ocupada. Inténtelo de nuevo.")
            

def mov_caballo_b(a, b, tablero) -> None:
    """Mueve el caballo blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    pre:
    - a y b son enteros en el rango del tablero (0-7), representando la fila y columna de la posición
    actual del caballo blanco.

    post:
    - Realiza el movimiento si es válido, capturando piezas enemigas si corresponde.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_caballo(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c] != '':
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            continue
        
def mov_caballo_n(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_caballo(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c] != '':
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
                tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            continue

def mov_reina_b(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_reina(a, b, fin_f, fin_c, tablero):
            # Captura diagonal
            if tablero[fin_f][fin_c] != '':
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")
        
        
def mov_reina_n(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_reina(a, b, fin_f, fin_c, tablero):
            if tablero[fin_f][fin_c] != '':
                print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")


def mov_rey_b(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_rey(a, b, fin_f, fin_c):
            # Capturar pieza enemiga si la hay
            if tablero[fin_f][fin_c] != '':
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            continue
        
def mov_rey_n(a, b, tablero) -> None:
    while True:
        fin_f, fin_c = obtener_coordenadas()
        
        if val.validar_rey(a, b, fin_f, fin_c):
            # Capturar pieza enemiga si la hay
            if tablero[fin_f][fin_c] != '':
                print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            continue


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
