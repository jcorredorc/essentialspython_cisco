from platform import machine
from random import randrange, choice

allowed_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
machine_options = allowed_fields[:]
board_index = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
               "4": (1, 0), "5": (1, 1), "6": (1, 2),
               "7": (2, 0), "8": (2, 1), "9": (2, 2)}


def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola
    #
    print("""
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   %s   |   %s   |   %s   |
    |       |       |       |
    +-------+-------+-------+"""
          % (board[0][0], board[0][1], board[0][2],
             board[1][0], board[1][1], board[1][2],
             board[2][0], board[2][1], board[2][2]))


def EnterMove(board):
    #
    # la función acepta el estado actual del tablero y pregunta al usuario
    # acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario
    #
    user_move = 0

    while user_move not in allowed_fields:
        user_move = int(input("ingresa tu movimiento: "))
    field_test = board[board_index.get(str(user_move))[
        0]][board_index.get(str(user_move))[1]]
    if field_test not in ['O', 'X']:
        board[board_index.get(str(user_move))[0]
              ][board_index.get(str(user_move))[1]] = "O"
        # DisplayBoard(board)
    else:
        print("U: movimiento no permitido, ya ha sido jugado")
        EnterMove(board)
    return board


def MakeListOfFreeFields(board):
    #
    # la función examina el tablero y construye una lista de todos los cuadros
    # vacíos
    # la lista esta compuesta por tuplas, cada tupla es un par de números que
    # indican la fila y columna
    #
    free_fields = []
    play_fields = ["X", "O"]
    for r in range(3):
        for c in range(3):
            if board[r][c] not in play_fields:
                free_fields.append((r, c))
    return free_fields


def VictoryFor(board, sign):
    #
    # la función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    #
    row1 = (board[0][0], board[0][1], board[0][2])
    row2 = (board[1][0], board[1][1], board[1][2])
    row3 = (board[2][0], board[2][1], board[2][2])
    col1 = (board[0][0], board[1][0], board[2][0])
    col2 = (board[0][1], board[1][1], board[2][1])
    col3 = (board[0][2], board[1][2], board[2][2])
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])

    if sign == "X":
        test = ("X", "X", "X")
    else:
        test = ("O", "O", "O")

    if row1 == test or row2 == test or row3 == test or \
       col1 == test or col2 == test or col3 == test or \
       diag1 == test or diag2 == test:
        if sign == "X":
            # print("gana la maquina ")
            return "X"
        else:
            # print("ganaste")
            return "O"
    else:
        # """ empate o aun se juega """
        if MakeListOfFreeFields(board) == []:
            #print("Empate: ", MakeListOfFreeFields(board))
            return "tie"  # 'empate'
        else:
            #print("no gana", sign, "aun :P")
            return None


def DrawMove(board):
    #
    # la función dibuja el movimiento de la maquina y actualiza el tablero
    #
    # machine_move = randrange(1, 9)
    global machine_options
    machine_move = choice(machine_options)
    machine_options.pop(machine_options.index(machine_move))
    # print(machine_options)
    # while user_move not in allowed_fields:
    #     user_move=int(input("ingresa tu movimiento: "))
    field_test = board[board_index.get(str(machine_move))[
        0]][board_index.get(str(machine_move))[1]]
    if field_test not in ['O', 'X']:
        board[board_index.get(str(machine_move))[0]
              ][board_index.get(str(machine_move))[1]] = "X"
        # DisplayBoard(board)
    else:
        # print("M: movimiento no permitido, ya ha sido jugado")
        DrawMove(board)
    return board


def CreateBoard():
    item = 0
    board = [[0 for x in range(3)] for y in range(3)]
    # print(board)
    for r in range(3):
        for c in range(3):
            item += 1
            board[r][c] = item
    # juega la maquina al inicio
    board[1][1] = "X"
    return board


if __name__ == "__main__":
    item = 0
    board = [[0 for x in range(3)] for y in range(3)]
    # print(board)
    for r in range(3):
        for c in range(3):
            item += 1
            board[r][c] = item
    # print(board)
    board[0][0] = "X"
    board[0][1] = "O"
    board[0][2] = "X"
    board[1][0] = "X"
    board[1][1] = "O"
    board[1][2] = "O"
    board[2][0] = "O"
    board[2][1] = "X"
    board[2][2] = "X"
    DisplayBoard(board)
    # for i in range(10):
    #     print(randrange(8))
    # jugada_maquina= randrange(8)
    # print(jugada_maquina)
    # EnterMove(board)
    # DrawMove(board)
    VictoryFor(board, "X")
    VictoryFor(board, "O")
