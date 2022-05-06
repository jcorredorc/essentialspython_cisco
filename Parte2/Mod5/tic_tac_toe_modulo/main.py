import tic_tac_toe as triqui

tablero = triqui.CreateBoard()
triqui.DisplayBoard(tablero)
while True:
    tablero = triqui.EnterMove(tablero)
    triqui.DisplayBoard(tablero)
    if triqui.VictoryFor(tablero, "O") == "O":
        print("==============")
        print(" Gana usuario")
        print("==============")
        break
    tablero = triqui.DrawMove(tablero)
    triqui.DisplayBoard(tablero)
    if triqui.VictoryFor(tablero, "X") == "X":
        print("===============")
        print(" Gana máquina")
        print("===============")
        break
    # si es empate sale del ciclo
    if triqui.VictoryFor(tablero, "O") == "tie":
        print("===============")
        print("   Empate !!!")
        print("===============")
        break
    # else:
    #     print(triqui.VictoryFor(tablero, "O"))
# print("FIN")
