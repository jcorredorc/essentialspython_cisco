import tic_tac_toe

tablero = tic_tac_toe.CreateBoard()
# estado_juego = True 
tic_tac_toe.DisplayBoard(tablero)
while True:
    tablero = tic_tac_toe.EnterMove(tablero)
    tic_tac_toe.DisplayBoard(tablero)
    if  tic_tac_toe.VictoryFor(tablero,"O") == "O":
        print("gana usuario")
        break
    tablero = tic_tac_toe.DrawMove(tablero)
    tic_tac_toe.DisplayBoard(tablero)
    if  tic_tac_toe.VictoryFor(tablero,"X") == "X":
        print("gana maquina")
        break
    # si es empate sale del ciclo
    if  tic_tac_toe.VictoryFor(tablero,"O") == "tie":
        print("empate")
        break
print("FIN")

    