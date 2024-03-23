import piece_Move_2



def schach(layout):

    wK  = "wK "
    sK  = "sK "


    white_Pieces = ["wT ", "wL ", "wS ", "wK ", "wKK", "wS ", "wL ", "wT ", "wB ", "___"]
    black_Pieces = ["sT ", "sL ", "sS ", "sK ", "sKK", "sS ", "sL ", "sT ", "sB ", "___"]
    w_chk_Piece = []
    s_chk_Piece = []
    layout_K = []
    king_Pos = []
    finish = False

    for n in range(9):
        for k in range(9):
            if layout[n][k] == "wK ":
                king_Pos.append([n, k])
            if layout[n][k] == "sK ":
                king_Pos.append([n, k])
    if len(king_Pos) == 1:
        if wK == layout[king_Pos[0][0]][king_Pos[0][1]]:
            print("Weiß gewinnt!")
            return True
        if sK == layout[king_Pos[0][0]][king_Pos[0][1]]:
            print("Schwarz gewinnt!")
            return True
        if len(king_Pos) == 0:
            print("Es ist unentschieden!")
        return False

    for n in range(9):
        for k in range(9):
                if piece_Move_2.make_move([n, k], king_Pos[0], layout, None, None):
                    w_chk_Piece = [n, k]
                if piece_Move_2.make_move([n, k], king_Pos[1], layout, None, None):
                    s_chk_Piece = [n, k]


    if w_chk_Piece == [] and s_chk_Piece == []:
        print("Nächster zug")
    elif w_chk_Piece != []:
        print(layout[w_chk_Piece[0]][w_chk_Piece[1]], "setzt den König schach!")
        finish = False
    elif s_chk_Piece != []:
        print(layout[s_chk_Piece[0]][s_chk_Piece[1]], "setzt den König schach!")
        finish = False

    return finish