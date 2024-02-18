
import Validaciones as val
from typing import List

def movimiento_blanco(fila: int, columna: int, tablero: List[List[str]]) -> bool:
    """Compara el string en la ubicación designada del tablero y llama la función correspondiente
    si es una pieza blanca.
    
    Precondición:
    -La ubicación contiene una pieza blanca.
    
    Postcondición:
    -Si no es una pieza blanca devuelve False.
    -Si es una pieza blance, llama otra función para moverla.
    """
    if not(tablero[fila][columna].endswith('b')):
        print('No hay una pieza blanca en esa posición')
        return True
    elif tablero[fila][columna] == 'peonb':
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
    

def movimiento_negro(fila: int, columna: int, tablero: List[List[str]]) -> bool:
    """Compara el string en la ubicación designada del tablero y llama la función correspondiente
    si es una pieza negra.
    
    Precondición:
    -La ubicación contiene una pieza negra.
    
    Postcondición:
    -Si no es una pieza negra devuelve False.
    -Si es una pieza negra, llama otra función para moverla.
    """
    if not(tablero[fila][columna].endswith('n')):
        print('No hay una pieza negra en esa posición')
        return True
    elif tablero[fila][columna] == 'peonn':
        mov_peon_n(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'torren':
        mov_torre_n(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'alfiln':
        mov_alfil_n(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'caballon':
        mov_caballo_n(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reinan':
        mov_reina_n(fila, columna, tablero)
        return False
    elif tablero[fila][columna] == 'reyn':
        mov_rey_n(fila, columna, tablero)
        return False
    else:
        print('No hay una pieza negra en esa posición')
        return True

def obtener_coordenadas() -> tuple:
    """Obtiene las coordenadas (fila, columna) del usuario.

    Precondición:

    Postcondición:
    - Devuelve un tuple con dos enteros representando las coordenadas (fila, columna)
    ingresadas por el usuario.
    """
    while True:
        try:
            fila = int(input('Fila objetivo: '))
            columna = int(input('Columna objetivo: '))
            return fila, columna
        except ValueError:
            print('Ingrese coordenadas válidas (números enteros).')


def mov_peon_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el peón blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del peón blanco en el tablero.

    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        if tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif val.validar_peon(a, b, fin_f, fin_c, tablero):
            print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            contador += 1
            continue


def mov_peon_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el peón negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    -Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del peón negro en el tablero.

    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif val.validar_peon(a, b, fin_f, fin_c, tablero):
            print(f"¡Pieza {tablero[fin_f][fin_c]} eliminada!")
            tablero[fin_f][fin_c] = ''
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print("Movimiento inválido.")
            contador += 1
            continue



def mov_torre_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve la torre blanca desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual de la torre blanca en
    el tablero.

    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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
        elif (tablero[fin_f][fin_c] == 'reyb') and diccionario_enroque['enroque_blanco'] and valido:
            print('¡Enroque!')
            diccionario_enroque['enroque_blanco'] = False
            if fin_c < b:
                tablero[fin_f][fin_c + 2] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c + 1] = tablero[a][b]
                tablero[a][b] = ''
            else:
                tablero[fin_f][fin_c - 2] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c - 1] = tablero[a][b]
                tablero[a][b] = ''
            break
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


def mov_torre_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve la torre negra desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual de la torre negra en
    el tablero.

    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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
        elif (tablero[fin_f][fin_c] == 'reyn') and diccionario_enroque['enroque_negro'] and valido:
            print('¡Enroque!')
            diccionario_enroque['enroque_negro'] = False
            if fin_c < b:
                tablero[fin_f][fin_c + 2] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c + 1] = tablero[a][b]
                tablero[a][b] = ''
            else:
                tablero[fin_f][fin_c - 2] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c - 1] = tablero[a][b]
                tablero[a][b] = ''
            break
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



def mov_alfil_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el alfil blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del alfil blanco en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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


def mov_alfil_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el alfil negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del alfil negro en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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
            

def mov_caballo_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el caballo blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    Precondición:
    - a y b son enteros, representando la fila y columna de la posición actual del caballo blanco.

    Postcondición:
    - Realiza el movimiento si es válido
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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
        
def mov_caballo_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve el caballo negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.

    Precondición:
    - a y b son enteros, representando la fila y columna de la posición actual del caballo negro.

    Postcondición:
    - Realiza el movimiento si es válido
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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

def mov_reina_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve la reina blanca desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual de la reina blanca en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido para el alfil o la torre.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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
        
        
def mov_reina_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve la reina negra desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual de la reina negra en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido para el alfil o la torre.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
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


def mov_rey_b(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve al rey blanco desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del rey blanco en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_rey(a, b, fin_f, fin_c)
        
        if tablero[fin_f][fin_c].endswith('b'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'torreb') and diccionario_enroque['enroque_blanco'] and valido:
            print('¡Enroque!')
            diccionario_enroque['enroque_blanco'] = False
            if fin_c < b:
                tablero[fin_f][fin_c - 1] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c - 2] = tablero[a][b]
                tablero[a][b] = ''
            else:
                tablero[fin_f][fin_c + 1] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c + 2] = tablero[a][b]
                tablero[a][b] = ''
            break
        elif tablero[fin_f][fin_c].endswith('n') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            diccionario_enroque['enroque_blanco'] = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            diccionario_enroque['enroque_blanco'] = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue
        
def mov_rey_n(a: int, b: int, tablero: List[List[str]]) -> None:
    """Mueve al rey negro desde la posición (a, b) a una posición objetivo ingresada por el usuario.
    
    Precondición:
    - a y b son enteros representando la fila y columna de la posición actual del rey negro en
    el tablero.
    
    Postcondición:
    - Realiza el movimiento si es válido.
    - Imprime un mensaje de error si el movimiento no es válido.
    """
    contador = 0
    while True:
        #Si no se mueve correctamente la pieza, se salta el turno
        if contador > 4:
            print('Demasiados intentos')
            return
        fin_f, fin_c = obtener_coordenadas()
        
        valido = val.validar_rey(a, b, fin_f, fin_c)
        
        if tablero[fin_f][fin_c].endswith('n'):
            print('Movimiento inválido.')
            contador += 1
            continue
        elif (tablero[fin_f][fin_c] == 'torren') and diccionario_enroque['enroque_negro'] and valido:
            print('¡Enroque!')
            diccionario_enroque['enroque_negro'] = False
            if fin_c < b:
                tablero[fin_f][fin_c - 1] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c - 2] = tablero[a][b]
                tablero[a][b] = ''
            else:
                tablero[fin_f][fin_c + 1] = tablero[fin_f][fin_c]
                tablero[fin_f][fin_c] = ''
                tablero[fin_f][fin_c + 2] = tablero[a][b]
                tablero[a][b] = ''
            break
        elif tablero[fin_f][fin_c].endswith('b') and valido:
            print(f'¡Pieza {tablero[fin_f][fin_c]} eliminada!')
            tablero[fin_f][fin_c] = ''
            diccionario_enroque['enroque_negro'] = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        elif tablero[fin_f][fin_c].endswith('') and valido:
            diccionario_enroque['enroque_negro'] = False
            tablero[a][b], tablero[fin_f][fin_c] = tablero[fin_f][fin_c], tablero[a][b]
            return
        else:
            print('Movimiento inválido.')
            contador += 1
            continue

def promocion(tablero: List[List[str]]) -> None:
    """Promociona a un peon si llega al otro lado del tablero
    
    Precondición:
    
    Postcondición:
    -Cambia un peon por otra pieza a elección del usuario
    """
    #Si un peon blanco llega a la parte superior del tablero, promociona
    if 'peonb' in tablero[0]:
        print('Peon blanco promociona')
        promocionado = promos[int(input('1-Torre, 2-Caballo, 3-Alfil, 4-Reina: ')) - 1]
        tablero[0][tablero[0].index('peonb')] = promocionado + 'b'
    
    #Si un peon negro llega a la parte inferior del tablero, promociona
    if 'peonn' in tablero[-1]:
        print('Peon negro promociona')
        promocionado = promos[int(input('1-Torre, 2-Caballo, 3-Alfil, 4-Reina: ')) - 1]
        tablero[-1][tablero[-1].index('peonn')] = promocionado + 'n'

promos = ('torre', 'caballo', 'alfil', 'reina')

diccionario_enroque = {'enroque_blanco': True, 'enroque_negro': True}
