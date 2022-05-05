from random import randrange

allowed_fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board_index = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
               "4": (1, 0), "5": (1, 1), "6": (1, 2),
               "7": (2, 0), "8": (2, 1), "9": (2, 2)}


def DisplayBoard(board):
    #
    # la función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola
    #
    horizontal_line = "+"+7*"-"
    horizontal_space = "|"+7*" "
    play_line_1 = "|" + 3*" " + str(board[0][0]) + 3*" " + \
                  "|" + 3*" " + str(board[0][1]) + 3*" " + \
                  "|" + 3*" " + str(board[0][2]) + 3*" " + "|"
    play_line_2 = "|" + 3*" " + str(board[1][0]) + 3*" " + \
                  "|" + 3*" " + str(board[1][1]) + 3*" " + \
                  "|" + 3*" " + str(board[1][2]) + 3*" " + "|"
    play_line_3 = "|" + 3*" " + str(board[2][0]) + 3*" " + \
                  "|" + 3*" " + str(board[2][1]) + 3*" " + \
                  "|" + 3*" " + str(board[2][2]) + 3*" " + "|"

    print(3*horizontal_line + "+")
    print(3*horizontal_space + "|")
    print(play_line_1)
    print(3*horizontal_space + "|")
    # ----------
    print(3*horizontal_line + "+")
    print(3*horizontal_space + "|")
    print(play_line_2)
    print(3*horizontal_space + "|")
    # ----------
    print(3*horizontal_line + "+")
    print(3*horizontal_space + "|")
    print(play_line_3)
    print(3*horizontal_space + "|")
    # ----------
    print(3*horizontal_line + "+")


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
        DisplayBoard(board)
    else:
        print("movimiento no permitido, ya ha sido jugado")
        EnterMove(board)


def MakeListOfFreeFields(board):
    #
    # la función examina el tablero y construye una lista de todos los cuadros
    # vacíos
    # la lista esta compuesta por tuplas, cada tupla es un par de números que
    # indican la fila y columna
    #
    free_fields = []
    play_fields = ("X", "O", "x", "o", "0")
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
    row1 = tuple(board[0][:])
    row2 = tuple(board[1][:])
    row3 = tuple(board[2][:])
    col1 = tuple(board[:][0])
    col2 = tuple(board[:][1])
    col3 = tuple(board[:][2])
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])

    if sign == "X":
        test = ("X", "X", "X")
    else:
        test = ("O", "O", "O")

    # print(row1)
    # for r in range(3):
    #     for c in range(3):
    #         tuple(board[r][:])

    if row1 == test or row2 == test or row3 == test or \
       col1 == test or col2 == test or col3 == test or \
       diag1 == test or diag2 == test:
        if sign == "X":
            print("gana la maquina ")
        else:
            print("ganaste")
    else:
        print("no gana nadie, aun")


def DrawMove(board):
    #
    # la función dibuja el movimiento de la maquina y actualiza el tablero
    #
    machine_move = randrange(1, 9)
    # while user_move not in allowed_fields:
    #     user_move=int(input("ingresa tu movimiento: "))
    field_test = board[board_index.get(str(machine_move))[
        0]][board_index.get(str(machine_move))[1]]
    if field_test not in ['O', 'X']:
        board[board_index.get(str(machine_move))[0]
              ][board_index.get(str(machine_move))[1]] = "X"
        DisplayBoard(board)
    else:
        print("movimiento no permitido, ya ha sido jugado")
        DrawMove(board)


# list = [x for x in range(1, 10)]
# print(list)

item = 0
board = [[0 for x in range(3)] for y in range(3)]
# print(board)
for r in range(3):
    for c in range(3):
        item += 1
        board[r][c] = item
# print(board)
board[0][0] = "X"
board[1][1] = "X"
board[2][2] = "X"
DisplayBoard(board)
# for i in range(10):
#     print(randrange(8))
# jugada_maquina= randrange(8)
# print(jugada_maquina)
EnterMove(board)
DrawMove(board)
VictoryFor(board, "X")
