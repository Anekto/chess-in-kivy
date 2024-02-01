'''Get coordinates like [1] [8] to move the piece to that position'''

wB  = "wB "
wT  = "wT "
wL  = "wL "
wS  = "wS "
wK  = "wK "
wKK = "wKK"
sB  = "sB "
sT  = "sT "
sL  = "sL "
sS  = "sS "
sK  = "sK "
sKK = "sKK"


white_Pieces = [wT, wL, wS, wK, wKK, wS, wL, wT, wB, "___"]
black_Pieces = [sT, sL, sS, sK, sKK, sS, sL, sT, sB, "___"]

def pawn(new_Pos, pos_V, layout, piece_pos, dest_pos):

    valid_move = False

    if wB == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 1 and layout[dest_pos[0]][dest_pos[1]] == white_Pieces[9]:
            valid_move = True
            if new_Pos[1] >= 1:
                valid_move = False
        if new_Pos[1] == 1 and layout[dest_pos[0]][dest_pos[1]] in black_Pieces[0:9]:
            valid_move = True
            if new_Pos[0] != 1:
                valid_move = False
        if new_Pos[0] == 2 and layout[piece_pos[0]][piece_pos[1]] in layout[2][piece_pos[1]]:
            valid_move = True
            if layout[dest_pos[0]][dest_pos[1]] in black_Pieces[0:9]:
                valid_move = False
            if layout[dest_pos[0]][dest_pos[1]] in white_Pieces[0:9]:
                valid_move = False
            if new_Pos[1] >= 1:
                valid_move = False
        if pos_V[0] < 0:
            valid_move = False
        return valid_move

    if sB == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 1 and layout[dest_pos[0]][dest_pos[1]] == black_Pieces[9]:
            valid_move = True
            if new_Pos[1] >= 1:
                valid_move = False
        if new_Pos[1] == 1 and layout[dest_pos[0]][dest_pos[1]] in white_Pieces[0:9]:
            valid_move = True
            if new_Pos[0] != 1:
                valid_move = False
        if new_Pos[0] == 2 and layout[piece_pos[0]][piece_pos[1]] in layout[7][piece_pos[1]]:
            valid_move = True
            if layout[dest_pos[0]][dest_pos[1]] in white_Pieces[0:9]:
                valid_move = False
            if layout[dest_pos[0]][dest_pos[1]] in black_Pieces[0:9]:
                valid_move = False
            if new_Pos[1] >= 1:
                valid_move = False
        if pos_V[0] > 0:
            valid_move = False
        return valid_move


def tower(new_Pos, pos_V, layout, piece_pos, dest_pos):

    valid_move = False

    if wT == layout[piece_pos[0]][piece_pos[1]]:
        if layout[dest_pos[0]][dest_pos[1]] in black_Pieces:
            valid_move = True

            if new_Pos[0] != 0 and new_Pos[1] == 0:
                for n in range(pos_V[0], 0, -1):
                    if n == 0 or n == new_Pos[0]:
                        continue
                    if layout[piece_pos[0] + n][piece_pos[1]] == black_Pieces[9]:

                        if valid_move == False:
                            break
                    elif layout[piece_pos[0] + n][piece_pos[1]] in black_Pieces[0:9]:
                        valid_move = False
                    else:
                        valid_move = False
            elif new_Pos[1] != 0 and new_Pos[0] == 0:
                for n in range(pos_V[1], 0, -1):
                    if n == 0 or n == new_Pos[1]:
                        continue
                    if layout[piece_pos[0]][piece_pos[1] + n] == black_Pieces[9]:
                        if valid_move == False:
                            break
                    elif layout[piece_pos[0]][piece_pos[1] + n] in black_Pieces[0:9]:
                        valid_move = False
                    else:
                        valid_move = False
            elif new_Pos[0] != 0 and new_Pos[1] != 0:
                valid_move = False

    if sT == layout[piece_pos[0]][piece_pos[1]]:
        if layout[dest_pos[0]][dest_pos[1]] in white_Pieces:
            valid_move = True

            if new_Pos[0] != 0 and new_Pos[1] == 0:
                for n in range(pos_V[0], 0, -1):
                    if n == 0 or n == new_Pos[0]:
                        continue
                    if layout[piece_pos[0] + n][piece_pos[1]] == white_Pieces[9]:

                        if valid_move == False:
                            break
                    elif layout[piece_pos[0] + n][piece_pos[1]] in white_Pieces[0:9]:
                        valid_move = False
                    else:
                        valid_move = False
            elif new_Pos[1] != 0 and new_Pos[0] == 0:
                for n in range(pos_V[1], 0, -1):
                    if n == 0 or n == new_Pos[1]:
                        continue
                    if layout[piece_pos[0]][piece_pos[1] + n] == white_Pieces[9]:
                        if valid_move == False:
                            break
                    elif layout[piece_pos[0]][piece_pos[1] + n] in white_Pieces[0:9]:
                        valid_move = False
                    else:
                        valid_move = False
            elif new_Pos[0] != 0 and new_Pos[1] != 0:
                valid_move = False

    return valid_move

def slider(new_Pos, pos_V, layout, piece_pos, dest_pos):

        # Pos1,Pos2 [8, 6] [3, 1]
        # PIECE sL  [5, 5] [-5, -5] [8, 6] [3, 1]

    valid_move = False

    print( "PIECE", layout[piece_pos[0]][piece_pos[1]], new_Pos, pos_V, piece_pos, dest_pos )

    if wL == layout[piece_pos[0]][piece_pos[1]]:
        if layout[dest_pos[0]][dest_pos[1]] in black_Pieces:
            valid_move = True
            if new_Pos[0] == new_Pos[1]: # if smaller than zero
                if pos_V[0] < 0:
                    for n in range(pos_V[0], 0, -1):
                        print("n:", n , "new_POS:", new_Pos[1])
                        print("Layout Position",layout[piece_pos[0] + n][piece_pos[1] + n])
                        if n == 0 or n == new_Pos[1]:
                            continue
                        if layout[piece_pos[0] + n][piece_pos[1] + n] == black_Pieces[9]:
                            continue
                        elif layout[piece_pos[0] + n][piece_pos[1] + n] in white_Pieces[0:9]:
                            valid_move = False
                        else:
                            valid_move = False

                elif pos_V[1] < 0:
                    for n in range(pos_V[1], 0, -1):
                        print("n:", n , "new_POS:", new_Pos[1])
                        print("Layout Position",layout[piece_pos[0] + n][piece_pos[1] + n])
                        if n == 0 or n == new_Pos[1]:
                            continue
                        if layout[piece_pos[0] + n][piece_pos[1] + n] == black_Pieces[9]:
                            continue
                        elif layout[piece_pos[0] + n][piece_pos[1] + n] in white_Pieces[0:9]:
                            valid_move = False
                        else:
                            valid_move = False
           
            else:
                valid_move = False

    if sL == layout[piece_pos[0]][piece_pos[1]]:
        if layout[dest_pos[0]][dest_pos[1]] in white_Pieces:
            valid_move = True
            if new_Pos[0] == new_Pos[1]: # if smaller than zero
                if pos_V[0] < 0:
                    for n in range(pos_V[0], 0, -1):
                        print("n:", n , "new_POS:", new_Pos[1])
                        print("Layout Position",layout[piece_pos[0] + n][piece_pos[1] + n])
                        if n == 0 or n == new_Pos[1]:
                            continue
                        if layout[piece_pos[0] + n][piece_pos[1] + n] == white_Pieces[9]:
                            continue
                        elif layout[piece_pos[0] + n][piece_pos[1] + n] in black_Pieces[0:9]:
                            valid_move = False
                        else:
                            valid_move = False
                            
                elif pos_V[1] < 0:
                    for n in range(pos_V[1], 0, -1):
                        print("n:", n , "new_POS:", new_Pos[1])
                        print("Layout Position",layout[piece_pos[0] + n][piece_pos[1] + n])
                        if n == 0 or n == new_Pos[1]:
                            continue
                        if layout[piece_pos[0] + n][piece_pos[1] + n] == white_Pieces[9]:
                            continue
                        elif layout[piece_pos[0] + n][piece_pos[1] + n] in black_Pieces[0:9]:
                            valid_move = False
                        else:
                            valid_move = False
           
            else:
                valid_move = False


    return valid_move

def horse(new_Pos, pos_V, layout, piece_pos, dest_pos):

    valid_move = False

    if wS == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 2 and new_Pos[1] == 1:
            if layout[dest_pos[0]][dest_pos[1]] in black_Pieces:
                valid_move = True
        if new_Pos[0] == 1 and new_Pos[1] == 2:
            if layout[dest_pos[0]][dest_pos[1]] in black_Pieces:
                valid_move = True

    if sS == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 2 and new_Pos[1] == 1:
            if layout[dest_pos[0]][dest_pos[1]] in white_Pieces:
                valid_move = True
        if new_Pos[0] == 1 and new_Pos[1] == 2:
            if layout[dest_pos[0]][dest_pos[1]] in white_Pieces:
                valid_move = True

    return valid_move

def king (new_Pos, pos_V, layout, piece_pos, dest_pos):

    valid_move = False

    if wK == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 1 or  new_Pos[1] == 1:
            if layout[dest_pos[0]][dest_pos[1]] in black_Pieces:
                valid_move = True

    if sK == layout[piece_pos[0]][piece_pos[1]]:
        if new_Pos[0] == 1 or  new_Pos[1] == 1:
            if layout[dest_pos[0]][dest_pos[1]] in white_Pieces:
                valid_move = True

    return valid_move

def queen(new_Pos, pos_V, layout, piece_pos, dest_pos):

    valid_move = False

    if slider(new_Pos, pos_V, layout, piece_pos, dest_pos) or tower(new_Pos, pos_V, layout, piece_pos, dest_pos):
        valid_move = True

    return valid_move



