
def validar_torre(inicio_f, inicio_c, final_f, final_c, tablero) -> bool:
    """
    Valida si el movimiento de la torre desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).

    Postcondición:
    - Devuelve True si el movimiento es válido para una torre, es decir, si se realiza en la misma fila o columna
      y no hay piezas intermedias.
    - Devuelve False si el movimiento no es válido.
    """
    if inicio_f == final_f:
        # Movimiento horizontal
        if final_c > inicio_c:
            direccion = 1
        else:
            direccion = -1
        for c in range(inicio_c + direccion, final_c, direccion):
            if tablero[inicio_f][c] != '':
                return False
        return True
    elif inicio_c == final_c:
        # Movimiento vertical
        if final_f > inicio_f:
            direccion = 1
        else:
            direccion = -1
            
        for f in range(inicio_f + direccion, final_f, direccion):
            if tablero[f][inicio_c] != '':
                return False
        return True
    else:
        return False


def validar_alfil(inicio_f, inicio_c, final_f, final_c, tablero) -> bool:
    """
    Valida si el movimiento del alfil desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).

    Postcondición:
    - Devuelve True si el movimiento es válido para un alfil, es decir, si se realiza en diagonal
      y no hay piezas intermedias.
    - Devuelve False si el movimiento no es válido.
    """
    if abs(final_f - inicio_f) == abs(final_c - inicio_c):
        # Movimiento en diagonal
        if final_f > inicio_f:
            direccion_f = 1
        else:
            direccion_f = -1
        
        if final_c > inicio_c:
            direccion_c = 1
        else:
            direccion_c = -1

        f, c = inicio_f + direccion_f, inicio_c + direccion_c
        while f != final_f and c != final_c:
            if tablero[f][c] != '':
                return False
            f += direccion_f
            c += direccion_c
        return True
    else:
        return False
    
def validar_caballo(inicio_f, inicio_c, final_f, final_c, tablero) -> bool:
    """
    Valida si el movimiento del caballo desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).

    Postcondición:
    - Devuelve True si el movimiento es válido para un caballo, es decir, si se realiza en forma de "L"
      y no hay piezas del mismo color en la casilla final.
    - Devuelve False si el movimiento no es válido.
    """
    if tablero[final_f][final_c] != '' and \
       (tablero[final_f][final_c].endswith('b') and tablero[inicio_f][inicio_c].endswith('b')) or \
       (tablero[final_f][final_c].endswith('n') and tablero[inicio_f][inicio_c].endswith('n')):
        return False
    elif (abs(final_f - inicio_f) == 2 and abs(final_c - inicio_c) == 1) or \
       (abs(final_f - inicio_f) == 1 and abs(final_c - inicio_c) == 2):
        # Movimiento en forma de "L"
        return True
    else:
        return False


def validar_reina(inicio_f, inicio_c, final_f, final_c, tablero) -> bool:
    """
    Valida si el movimiento de la reina desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).

    Postcondición:
    - Devuelve True si el movimiento es válido para una reina, es decir, si se realiza en la misma fila, columna
      o diagonal y no hay piezas intermedias.
    - Devuelve False si el movimiento no es válido.
    """
    return validar_torre(inicio_f, inicio_c, final_f, final_c, tablero) or validar_alfil(inicio_f, inicio_c, final_f, final_c, tablero)


def validar_rey(inicio_f, inicio_c, final_f, final_c) -> bool:
    """
    Valida si el movimiento del rey desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).

    Postcondición:
    - Devuelve True si el movimiento es válido para un rey, es decir, si se realiza en una casilla adyacente
      en cualquier dirección.
    - Devuelve False si el movimiento no es válido.
    """
    return (0 <= final_f <= 7) and (0 <= final_c <= 7) \
        and (abs(final_f - inicio_f) == 1 or abs(final_c - inicio_c) == 1) \
            and ((abs(final_f - inicio_f) + abs(final_c - inicio_c)) < 3)


def validar_peon(inicio_f, inicio_c, final_f, final_c, tablero) -> bool:
    """
    Valida si el movimiento del peón desde (inicio_f, inicio_c) hasta (final_f, final_c) es válido.

    Precondición:
    - Todas las coordenadas deben estar en el rango del tablero (0-7).
    - El color debe ser 'b' para blanco o 'n' para negro.

    Postcondición:
    - Devuelve True si el movimiento es válido para un peón, teniendo en cuenta el color,
      es decir, si se mueve hacia adelante y no hay piezas enemigas en la casilla de destino
      o si captura diagonalmente una pieza enemiga.
    - Devuelve False si el movimiento no es válido.
    """
    if (tablero[inicio_f][inicio_c])[-1] == 'b':
        return validar_p_blanco(inicio_f, inicio_c, final_f, final_c, tablero)
    elif (tablero[inicio_f][inicio_c])[-1] == 'n':
        return validar_p_negro(inicio_f, inicio_c, final_f, final_c, tablero)
    return False

def validar_p_blanco(inicio_f, inicio_c, final_f, final_c, tablero):
    # Peón blanco
    if (final_c == inicio_c) and ('' in tablero[final_f][final_c]) and ((final_f == inicio_f - 1) or ((final_f == inicio_f - 2) and (inicio_f == 6))):
        return True
    elif (abs(final_c - inicio_c) == 1) and (final_f == inicio_f - 1) and tablero[final_f][final_c].endswith('n'):
        return True
    else:
        return False

def validar_p_negro(inicio_f, inicio_c, final_f, final_c, tablero):
    # Peón negro
    if (final_c == inicio_c) and ('' in tablero[final_f][final_c]) and ((final_f == inicio_f + 1) or ((final_f == inicio_f + 2) and (inicio_f == 1))):
        return True
    elif (abs(final_c - inicio_c) == 1) and (final_f == inicio_f + 1) and tablero[final_f][final_c].endswith('b'):
        return True
    else:
        return False

def validar_victoria(color) -> bool:
    for fila in tablero:
        for elem in fila:
            if 'rey' in elem and elem.endswith(color):
                return True
    return False
